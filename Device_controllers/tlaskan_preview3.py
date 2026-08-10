import socket
import struct
import csv
import threading

# --- KONFIGURACE ---
TCP_IP = '192.168.10.96'  # Výchozí IP adresa zařízení
TCP_PORT = 23  # Port definovaný v tcp_server.c

REG_STREAM_EN = 18  # Adresa pro kontext_ram.tcp_stream_en
REG_MODE = 8  # Adresa pro kontext_ram.mode

# Hodnoty z ad_mode_t (ad7193.h)
AD_DISABLE = 0
AD_MAX_SPEED = 1

# Globální vlajka pro běh vlákna
streaming_active = False


def send_ram_write(sock, reg, value):
    """Pomocná funkce pro zápis 1 bytu do RAM přes tvůj AT příkaz"""
    # Zápis 1 bytu na daný registr
    cmd = f"AT+RAM_RW={reg},1\r\n"
    sock.sendall(cmd.encode('ascii'))

    # Čekáme na výzvu "Waiting for data..."
    response = sock.recv(1024).decode('ascii')
    if "Waiting" not in response:
        print(f"Chyba při čekání na data: {response}")
        return False

    # Odeslání samotné hodnoty v binárním tvaru (1 byte)
    sock.sendall(bytes([value]))

    # Čekáme na potvrzení OK
    response = sock.recv(1024).decode('ascii')
    if "OK" not in response:
        print(f"Chyba při zápisu: {response}")
        return False

    return True


def receive_stream_thread(sock, filename):
    """Vlákno, které běží na pozadí a sype data do CSV"""
    global streaming_active

    # Formát pevné části: < (little endian), H (header), I (packet_id), H (active_mask), B (sample_count)
    header_format = "<H I H B"
    header_size = struct.calcsize(header_format)

    print(f"\n[Stream] Očekávaná velikost hlavičky: {header_size} bajtů")

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Packet_ID", "Timestamp_us", "CH1", "CH2", "CH3", "CH4"])

        while streaming_active:
            try:
                # 1. SYNCHRONIZACE: Čteme po bajtech, dokud nenajdeme hlavičku 0xAAAA
                header_bytes = sock.recv(2)
                if not header_bytes: break

                while header_bytes != b'\xAA\xAA':
                    next_byte = sock.recv(1)
                    if not next_byte: break
                    header_bytes = header_bytes[1:] + next_byte

                if header_bytes != b'\xAA\xAA': break

                # 2. NAČTENÍ ZBYTKU HLAVIČKY (ID, mask, count) - zbývá 7 bajtů
                rest_of_header = bytearray()
                while len(rest_of_header) < (header_size - 2) and streaming_active:
                    chunk = sock.recv((header_size - 2) - len(rest_of_header))
                    if not chunk: break
                    rest_of_header.extend(chunk)

                if len(rest_of_header) != (header_size - 2):
                    break

                full_header = header_bytes + rest_of_header
                unpacked_header = struct.unpack(header_format, full_header)

                # Rozbalení proměnných z hlavičky
                packet_id = unpacked_header[1]
                active_mask = unpacked_header[2]
                sample_count = unpacked_header[3]

                # 3. ZJISTĚNÍ VELIKOSTI VZORKU PODLE MASKY
                num_active_channels = 0
                for i in range(4):
                    if active_mask & (1 << i):
                        num_active_channels += 1

                # Každý vzorek = 4 bajty (timestamp) + (počet aktivních kanálů * 4 bajty)
                sample_size = 4 + (num_active_channels * 4)
                payload_size = sample_count * sample_size

                # 4. NAČTENÍ CELÉHO PAYLOADU (DAT)
                payload_data = bytearray()
                while len(payload_data) < payload_size and streaming_active:
                    chunk = sock.recv(payload_size - len(payload_data))
                    if not chunk: break
                    payload_data.extend(chunk)

                if len(payload_data) == payload_size:
                    # 5. ZPRACOVÁNÍ JEDNOTLIVÝCH VZORKŮ DYNAMICKY
                    # Formát jednoho vzorku: <I (timestamp) a pak X krát I (podle počtu aktivních kanálů)
                    sample_format = "<I" + ("I" * num_active_channels)

                    offset = 0
                    for _ in range(sample_count):
                        sample_bytes = payload_data[offset: offset + sample_size]
                        unpacked_sample = struct.unpack(sample_format, sample_bytes)

                        t_stamp = unpacked_sample[0]

                        # Čtení kanálů. Pokud je kanál deaktivovaný, zapíše se None (prázdná buňka v CSV)
                        ch1, ch2, ch3, ch4 = None, None, None, None

                        val_idx = 1
                        if active_mask & (1 << 0):
                            ch1 = unpacked_sample[val_idx]
                            val_idx += 1
                        if active_mask & (1 << 1):
                            ch2 = unpacked_sample[val_idx]
                            val_idx += 1
                        if active_mask & (1 << 2):
                            ch3 = unpacked_sample[val_idx]
                            val_idx += 1
                        if active_mask & (1 << 3):
                            ch4 = unpacked_sample[val_idx]
                            val_idx += 1

                        writer.writerow([packet_id, t_stamp, ch1, ch2, ch3, ch4])
                        offset += sample_size

            except socket.timeout:
                continue
            except Exception as e:
                if streaming_active:
                    print(f"[Stream] Chyba: {e}")
                break

    print("[Stream] Zápis do CSV ukončen.")


# --- HLAVNÍ PROGRAM ---
if __name__ == "__main__":
    print("=== Tenzoscan TCP Test ===")

    # 1. Připojení k zařízení
    print(f"Připojuji k {TCP_IP}:{TCP_PORT}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)  # Nastavíme timeout pro bezpečné ukončování vlákna
    s.connect((TCP_IP, TCP_PORT))
    print("Připojeno!\n")

    input("Stiskni ENTER pro spuštění měření (AD_MAX_SPEED)...")

    # 2. Nastavení a spuštění
    print("Povoluji TCP stream v RAM...")
    send_ram_write(s, REG_STREAM_EN, 1)

    streaming_active = True
    thread = threading.Thread(target=receive_stream_thread, args=(s, "mereni_tenzoscan.csv"))
    thread.start()

    print("Zapínám ADC (AD_MAX_SPEED)...")
    send_ram_write(s, REG_MODE, AD_MAX_SPEED)

    # 3. Měření běží
    input("\nMěření probíhá. Data se ukládají do CSV.\nStiskni ENTER pro zastavení...")

    # 4. Zastavení a úklid
    print("\nVypínám ADC (AD_DISABLE)...")
    send_ram_write(s, REG_MODE, AD_DISABLE)

    print("Vypínám TCP stream v RAM...")
    send_ram_write(s, REG_STREAM_EN, 0)

    streaming_active = False
    thread.join()

    s.close()
    print("Spojení ukončeno. Hotovo.")