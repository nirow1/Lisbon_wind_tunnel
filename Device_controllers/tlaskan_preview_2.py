import socket
import struct
import csv
import threading
import time

# --- KONFIGURACE ---
# Dvě zařízení (můžeš jich přidat více)
DEVICES = ['192.168.1.96', '192.168.1.97']
TCP_PORT = 23

REG_STREAM_EN = 18
REG_MODE = 8

AD_DISABLE = 0
AD_MAX_SPEED = 1
AD_SPEED = 2

# Slovník pro vlajky běhu vláken, klíčem je IP adresa
streaming_active = {ip: False for ip in DEVICES}


def send_ram_write(sock, reg, value):
    """Pomocná funkce pro zápis 1 bytu do RAM přes AT příkaz"""
    cmd = f"AT+RAM_RW={reg},1\r\n"
    sock.sendall(cmd.encode('ascii'))

    response = sock.recv(1024).decode('ascii')
    if "Waiting" not in response:
        print(f"Chyba při čekání na data: {response}")
        return False

    sock.sendall(bytes([value]))

    response = sock.recv(1024).decode('ascii')
    if "OK" not in response:
        print(f"Chyba při zápisu: {response}")
        return False

    return True


def receive_stream_thread(ip, filename):
    """Vlákno, které naváže spojení, nastaví ADC a sype data do CSV pro konkrétní IP"""
    global streaming_active

    # Navázání spojení uvnitř vlákna
    print(f"[{ip}] Připojuji...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)
        s.connect((ip, TCP_PORT))
        print(f"[{ip}] Připojeno.")

        # Zapnutí streamu a měření přes kontextovou paměť RAM
        print(f"[{ip}] Povoluji TCP stream a ADC...")
        send_ram_write(s, REG_STREAM_EN, 1)
        send_ram_write(s, REG_MODE, AD_SPEED)

    except Exception as e:
        print(f"[{ip}] Nelze navázat spojení nebo nastavit měření: {e}")
        streaming_active[ip] = False
        return

    header_format = "<H I H B"
    header_size = struct.calcsize(header_format)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Packet_ID", "Timestamp_us", "CH1", "CH2", "CH3", "CH4"])

        while streaming_active[ip]:
            try:
                # 1. SYNCHRONIZACE
                header_bytes = s.recv(2)
                if not header_bytes: break

                while header_bytes != b'\xAA\xAA':
                    next_byte = s.recv(1)
                    if not next_byte: break
                    header_bytes = header_bytes[1:] + next_byte

                if header_bytes != b'\xAA\xAA': break

                # 2. NAČTENÍ ZBYTKU HLAVIČKY (packet_id, active_mask, sample_count)
                rest_of_header = bytearray()
                while len(rest_of_header) < (header_size - 2) and streaming_active[ip]:
                    chunk = s.recv((header_size - 2) - len(rest_of_header))
                    if not chunk: break
                    rest_of_header.extend(chunk)

                if len(rest_of_header) != (header_size - 2):
                    break

                full_header = header_bytes + rest_of_header
                unpacked_header = struct.unpack(header_format, full_header)

                packet_id = unpacked_header[1]
                active_mask = unpacked_header[2]
                sample_count = unpacked_header[3]

                # 3. ZJISTĚNÍ VELIKOSTI VZORKU PODLE BITOVÉ MASKY
                num_active_channels = 0
                for i in range(4):
                    if active_mask & (1 << i):
                        num_active_channels += 1

                sample_size = 4 + (num_active_channels * 4)
                payload_size = sample_count * sample_size

                # 4. NAČTENÍ CELÉHO DATOVÉHO PAYLOADU
                payload_data = bytearray()
                while len(payload_data) < payload_size and streaming_active[ip]:
                    chunk = s.recv(payload_size - len(payload_data))
                    if not chunk: break
                    payload_data.extend(chunk)

                if len(payload_data) == payload_size:
                    # 5. DYNAMICKÉ ZPRACOVÁNÍ VZORKŮ Z PAYLOADU
                    sample_format = "<I" + ("I" * num_active_channels)

                    offset = 0
                    for _ in range(sample_count):
                        sample_bytes = payload_data[offset: offset + sample_size]
                        unpacked_sample = struct.unpack(sample_format, sample_bytes)

                        t_stamp = unpacked_sample[0]

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
                if streaming_active[ip]:
                    print(f"[{ip}] Chyba streamu: {e}")
                break

    # Úklid po ukončení stahování ve vlákně
    print(f"[{ip}] Zastavuji měření a odpojuji zařízení...")
    try:
        send_ram_write(s, REG_STREAM_EN, 0)
        send_ram_write(s, REG_MODE, AD_DISABLE)
    except:
        pass
    s.close()
    print(f"[{ip}] Zápis do CSV ukončen a spojení zavřeno.")


# --- HLAVNÍ PROGRAM ---
if __name__ == "__main__":
    print("=== Tenzoscan Multi-TCP Test ===")

    input("Stiskni ENTER pro hromadné připojení ke všem zařízením a spuštění měření...\n")

    threads = []

    # Spuštění individuálních vláken pro všechny nakonfigurované IP adresy.
    for ip in DEVICES:
        streaming_active[ip] = True
        filename = f"mereni_tenzoscan_{ip.replace('.', '_')}.csv"
        t = threading.Thread(target=receive_stream_thread, args=(ip, filename))
        threads.append(t)
        t.start()

    input(
        "\n\nMěření probíhá (pokud se vlákna úspěšně připojila).\nData se ukládají do příslušných CSV.\nStiskni ENTER pro zastavení všech měření...\n\n")

    # Bezpečné zastavení vláken změnou vlajek a následné ukončení celého programu
    for ip in DEVICES:
        streaming_active[ip] = False

    for t in threads:
        t.join()

    print("Hotovo. Všechna měření z Tenzoskenů byla úspěšně ukončena.")