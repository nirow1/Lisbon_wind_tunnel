import csv
import os
import sys
import threading
import logging
import socket
import time

from PySide6.QtCore import Signal, QThread
from struct import unpack


class TlaskanController(QThread):
    PRESSURE_DATA = Signal(list)

    def __init__(self, ip="192.168.10.98"):
        super().__init__()
        self.connected = False
        self.ip = ip
        self.port = 23
        self.msg = ""
        self.zero_values = [0.0 for _ in range(16)]
        self.processed_pressure = []
        self.tlaskan = None
        self._request_thread = None
        self.csv_path = ""
        self._csv_file = None
        self._csv_writer = None

    def set_csv_path(self, path):
        self.csv_path = path if path else ""

    def _print_data_line(self, data):
        """Always rewrite console line 1; leave the cursor where it was."""
        text = " | ".join(f"{v:7.3f}" for v in data)
        # save cursor, go to (1,1), clear line, print, restore cursor
        sys.stdout.write(
            f"\033[s\033[1;1H\033[2KTLASKAN [{self.ip}]: {text}\033[u"
        )
        sys.stdout.flush()

    def _csv_filename(self):
        safe_ip = self.ip.replace(".", "_")
        name = f"tlaskan_data_{safe_ip}.csv"
        if self.csv_path:
            path = os.path.join(self.csv_path, name)
        else:
            path = name
        return os.path.abspath(path)

    def _open_csv(self):
        path = self._csv_filename()
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self._csv_file = open(path, "w", newline="", buffering=1)
        self._csv_writer = csv.writer(self._csv_file, delimiter=";")
        header = ["Timestamp_ms", "Packet_ID"]
        for i in range(12):
            header.extend([f"S{i}_Press", f"S{i}_Status"])
        self._csv_writer.writerow(header)
        self._csv_file.flush()
        print(f"CSV logging to: {path}")

    def _close_csv(self):
        if self._csv_file is not None:
            try:
                self._csv_file.flush()
                self._csv_file.close()
            except Exception:
                pass
            self._csv_file = None
            self._csv_writer = None

    def run(self):
        self._connect_to_tlaskan()

    def _connect_to_tlaskan(self):
        while not self.connected:
            try:
                self.tlaskan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tlaskan.connect((self.ip, self.port))
                self.connected = True
                self.tlaskan.send(b'AT+RAM_RW=5,1\x0d\x0a')
                self.tlaskan.send(b'\x01')
                self._start_communication()
                break
            except Exception as e:
                print(F"failed to connect to TLASKAN: {e}")
                time.sleep(2)

    def _start_communication(self):
        self._request_thread = threading.Thread(target=self._send_measure_request, daemon=True)
        self._request_thread.start()
        self._listen_to_tls()

    def _send_measure_request(self):
        while self.connected:
            time.sleep(0.1)
            try:
                self.tlaskan.send(b'AT+RAM_RW=6,72,BIN,?\x0d\x0a')
            except OSError:
                break

    def _listen_to_tls(self):
        self._open_csv()
        try:
            self.tlaskan.recv(1024)
            while self.connected:
                try:
                    msg = self.tlaskan.recv(1024)
                    if not msg:
                        break
                    self.msg = msg[22:94]
                    lenght = len(self.msg)
                    
                    if lenght != 72 and self.msg:
                        continue

                    tlaskan_data = unpack("=" + "BfB" * 12, self.msg)
                    timestamp_ms = int(time.time() * 1000)
                    row = [timestamp_ms, 0]
                    pressures = []
                    for i in range(12):
                        base = i * 3
                        press = float(tlaskan_data[base + 1]) * 249.089
                        status = tlaskan_data[base + 2]
                        row.extend([f"{press:.4f}", status])
                        pressures.append(press)
                    self._csv_writer.writerow(row)
                    self._csv_file.flush()
                    self.processed_pressure = [
                        round(pressures[i], 3) - self.zero_values[i]
                        for i in range(len(pressures))
                    ]
                    self._print_data_line(self.processed_pressure)
                    self.PRESSURE_DATA.emit(self.processed_pressure)
                except socket.timeout:
                    continue
                except OSError:
                    break
        finally:
            self._close_csv()

    def _set_ram_register_blind(self, reg, val):
        """Blind write for safe shutdown without waiting for a reply."""
        try:
            cmd = f"AT+RAM_RW={reg},1\r\n".encode("ascii")
            self.tlaskan.sendall(cmd)
            time.sleep(0.05)
            self.tlaskan.sendall(bytes([val]))
            time.sleep(0.05)
        except Exception as e:
            print(f"Blind write reg {reg} failed: {e}")

    def disconnect(self):
        self.connected = False
        if self._request_thread is not None:
            self._request_thread.join(timeout=1.0)
            self._request_thread = None

        if self.tlaskan is None:
            self._close_csv()
            return

        try:
            self.tlaskan.settimeout(None)
            self.tlaskan.setblocking(True)
            # Stop measurement on the device (same pattern as tlaskan_preview1)
            self._set_ram_register_blind(5, 0)
            self.tlaskan.close()
        except Exception as e:
            print(f"Error disconnecting TLASKAN: {e}")
        finally:
            self.tlaskan = None
            self._close_csv()

    def set_zero_values(self):
        if self.connected:
            print(self.processed_pressure)
            self.zero_values = [self.zero_values[i]+self.processed_pressure[i] for i in range(len(self.zero_values))]


if __name__ == '__main__':
    tls = TlaskanController()
    try:
        tls.run()
    except KeyboardInterrupt:
        print("\nStopping TLASKAN...")
    finally:
        tls.disconnect()
        print("TLASKAN connection closed.")
