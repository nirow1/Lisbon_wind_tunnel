import socket
import struct
import csv
import time
import threading

# Konfigurace Tlaskanů (Změněno na seznam)
IP_ADDRESSES = ['192.168.10.98']
PORT = 23
MEASURE_PERIOD = 1


def set_ram_register(sock, reg, val, length=1, ip_log=""):
    """
    Univerzální zápis do virtuální RAM Tlaskanu s podporou více bajtů.
    """
    cmd = f"AT+RAM_RW={reg},{length}\r\n".encode('ascii')
    sock.sendall(cmd)

    resp = sock.recv(1024)
    if b"Waiting for data" in resp:
        # Převedení hodnoty na bajty (little-endian pro STM32 procesory)
        val_bytes = val.to_bytes(length, byteorder='little')
        sock.sendall(val_bytes)

        resp = sock.recv(1024)
        if b"OK" in resp:
            print(f"[{ip_log}] [OK] Registr {reg} nastaven na {val}.")
            return True

    print(f"[{ip_log}] [ERR] Chyba nastavení registru {reg}.")
    return False


def set_ram_register_blind(sock, reg, val, ip_log=""):
    """Slepý zápis pro bezpečné odstavení bez čekání na odpověď"""
    try:
        cmd = f"AT+RAM_RW={reg},1\r\n".encode('ascii')
        sock.sendall(cmd)
        time.sleep(0.05)
        sock.sendall(bytes([val]))
        time.sleep(0.05)
    except Exception as e:
        print(f"[{ip_log}] Chyba při slepém zápisu reg {reg}: {e}")


def daq_worker(sock, stop_event, csv_filename, ip_address):
    """Pracovní vlákno pro kontinuální příjem dat a zápis do CSV."""
    sock.settimeout(0.5)

    try:
        with open(csv_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")

            # Sestavení hlavičky CSV
            header = ["Timestamp_ms", "Packet_ID"]
            for i in range(12):
                header.extend([f"S{i}_Press", f"S{i}_Status"])
            writer.writerow(header)

            while not stop_event.is_set():
                try:
                    # A) Přečtení hlavičky paketu (9 bajtů)
                    head_data = bytearray()
                    while len(head_data) < 9 and not stop_event.is_set():
                        chunk = sock.recv(9 - len(head_data))
                        if not chunk:
                            raise ConnectionError("Spojení ztraceno.")
                        head_data.extend(chunk)

                    if stop_event.is_set():
                        break

                    sync, pkt_id, mask, sample_count = struct.unpack("<HIHB", head_data)

                    if sync != 0xAAAA:
                        continue

                    # B) Výpočet velikosti Payloadu na základě masky
                    active_channels = [i for i in range(12) if (mask & (1 << i))]
                    sample_size = 4 + (len(active_channels) * 5)
                    payload_size = sample_count * sample_size

                    # C) Přečtení bloku dat
                    payload_data = bytearray()
                    while len(payload_data) < payload_size and not stop_event.is_set():
                        chunk = sock.recv(payload_size - len(payload_data))
                        if not chunk:
                            raise ConnectionError("Spojení ztraceno během čtení payloadu.")
                        payload_data.extend(chunk)

                    if stop_event.is_set():
                        break

                    # D) Rozbalení vzorků
                    offset = 0
                    for _ in range(sample_count):
                        timestamp = struct.unpack_from("<I", payload_data, offset)[0]
                        offset += 4

                        row = [timestamp, pkt_id]

                        for i in range(12):
                            if i in active_channels:
                                press, status = struct.unpack_from("<fB", payload_data, offset)
                                offset += 5
                                row.extend([f"{press:.4f}", status])
                            else:
                                row.extend(["", ""])

                        writer.writerow(row)

                except socket.timeout:
                    continue
                except Exception as e:
                    if not stop_event.is_set():
                        print(f"\n[{ip_address}] Chyba ve čtecím vlákně: {e}")
                    break

    except Exception as e:
        print(f"[{ip_address}] Kritická chyba workeru: {e}")


def main():
    print("Připojování k zařízením Tlaskan...")
    stop_event = threading.Event()

    # Seznam pro uchování aktivních připojení a jejich vláken
    devices = []

    # 1. Spuštění měření a streamu pro každou IP adresu
    for ip in IP_ADDRESSES:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            s.connect((ip, PORT))

            set_ram_register(s, 4, MEASURE_PERIOD, length=4, ip_log=ip)
            set_ram_register(s, 5, 1, ip_log=ip)
            set_ram_register(s, 46, 1, ip_log=ip)

            # Generování dynamického názvu CSV souboru
            safe_ip = ip.replace('.', '_')
            csv_filename = f'tlaskan_data_{safe_ip}.csv'

            print(f"[{ip}] Stream spuštěn. Zápis do {csv_filename}...")

            # 2. Vytvoření a spuštění dělnického vlákna pro aktuální IP
            worker_thread = threading.Thread(target=daq_worker, args=(s, stop_event, csv_filename, ip))
            worker_thread.daemon = True
            worker_thread.start()

            # Uložení do seznamu pro pozdější korektní ukončení
            devices.append((ip, s, worker_thread))

        except Exception as e:
            print(f"[{ip}] Nepodařilo se připojit: {e}")

    if not devices:
        print("Nepodařilo se navázat spojení s žádným zařízením. Ukončuji program.")
        return

    print("\nSběr dat běží... (Pro ukončení stiskni červený čtvereček v PyCharmu)")

    try:
        # Hlavní vlákno čeká na event a kontroluje stav pracovních vláken.
        while not stop_event.wait(0.1):
            all_dead = True
            for ip, s, thread in devices:
                if thread.is_alive():
                    all_dead = False

            # Pokud všechna vlákna "umřou", ukončíme hlavní smyčku
            if all_dead:
                print("\nVšechna čtecí vlákna neočekávaně skončila.")
                break

    except KeyboardInterrupt:
        print("\nZastavuji měření...")
    finally:
        # Plynulé ukončení
        stop_event.set()

        for ip, s, thread in devices:
            thread.join(timeout=2.0)

            try:
                s.setblocking(1)
                print(f"[{ip}] Vypínám stream a měření na straně Tlaskanu...")
                set_ram_register_blind(s, 46, 0, ip_log=ip)
                set_ram_register_blind(s, 5, 0, ip_log=ip)
                s.close()
            except Exception as e:
                print(f"[{ip}] Chyba při ukončování spojení: {e}")

        print("Všechna spojení ukončena.")


if __name__ == "__main__":
    main()