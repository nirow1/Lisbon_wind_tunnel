import csv
import os
import socket
import struct
import threading
import time

from PySide6.QtCore import QThread, Signal


class TensoScannerController(QThread):
    PRESSURE_DATA = Signal(list)

    REG_MODE = 8
    REG_STREAM_EN = 18
    AD_DISABLE = 0
    AD_MAX_SPEED = 1

    def __init__(self, ip="192.168.10.96"):
        super().__init__()
        self.connected = False
        self.ip = ip
        self.port = 23
        self.msg = ""
        self.zero_values = [0.0 for _ in range(4)]
        self.processed_pressure = []
        self.tenso_scan = None
        self._receive_thread = None
        self._rx_buffer = bytearray()
        self.csv_path = ""
        self._csv_file = None
        self._csv_writer = None

    def set_csv_path(self, path):
        self.csv_path = path if path else ""

    def run(self):
        while not self.connected:
            if self._connect():
                self._start_streaming()
                if self._receive_thread is not None:
                    self._receive_thread.join()
                return
            time.sleep(2)

    def _connect(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)
            sock.connect((self.ip, self.port))
            self.tenso_scan = sock
            self.connected = True
            self._rx_buffer.clear()
            # Previous sessions may leave the device streaming; stop and clear the socket.
            self._set_ram_register_blind(self.REG_MODE, self.AD_DISABLE)
            self._set_ram_register_blind(self.REG_STREAM_EN, 0)
            self._drain_socket()
            return True
        except Exception as e:
            print(f"Failed to connect to tenzoscan: {e}")
            self.tenso_scan = None
            self.connected = False
            return False

    def _drain_socket(self):
        if self.tenso_scan is None:
            return
        self._rx_buffer.clear()
        prev_timeout = self.tenso_scan.gettimeout()
        self.tenso_scan.settimeout(0.05)
        try:
            while True:
                chunk = self.tenso_scan.recv(4096)
                if not chunk:
                    break
        except socket.timeout:
            pass
        except OSError:
            pass
        finally:
            self.tenso_scan.settimeout(prev_timeout if prev_timeout is not None else 2.0)

    def _start_streaming(self):
        self._open_csv()
        try:
            # Complete both AT writes before the reader thread touches the socket.
            # send_ram_write keeps any trailing 0xAA payload in _rx_buffer.
            self.send_ram_write(self.REG_STREAM_EN, 1)
            self.send_ram_write(self.REG_MODE, self.AD_MAX_SPEED)
            self._receive_thread = threading.Thread(target=self._receive_stream, daemon=True)
            self._receive_thread.start()
        except Exception as e:
            print(f"Failed to start streaming: {e}")

    def _recv_at_response(self, token: bytes, max_bytes: int = 4096) -> bytes:
        """Read until an AT token appears; keep any trailing binary in _rx_buffer."""
        buf = bytearray()
        while token not in buf:
            if self._rx_buffer:
                buf.extend(self._rx_buffer)
                self._rx_buffer.clear()
                if token in buf:
                    break
            chunk = self.tenso_scan.recv(1024)
            if not chunk:
                raise ConnectionError("Socket closed while waiting for AT response")
            buf.extend(chunk)
            if len(buf) >= max_bytes and token not in buf:
                raise RuntimeError(
                    f"AT token {token!r} not found; got {bytes(buf[:32])!r}..."
                )

        start = buf.find(token)
        nl = buf.find(b"\n", start)
        end = nl + 1 if nl != -1 else start + len(token)
        self._rx_buffer.extend(buf[end:])
        return bytes(buf[:end])

    def send_ram_write(self, reg, value):
        cmd = f"AT+RAM_RW={reg},1\r\n"
        self.tenso_scan.sendall(cmd.encode("ascii"))
        self._recv_at_response(b"Waiting")
        self.tenso_scan.sendall(bytes([value]))
        self._recv_at_response(b"OK")

    def _set_ram_register_blind(self, reg, value):
        try:
            cmd = f"AT+RAM_RW={reg},1\r\n".encode("ascii")
            self.tenso_scan.sendall(cmd)
            time.sleep(0.05)
            self.tenso_scan.sendall(bytes([value]))
            time.sleep(0.05)
        except Exception as e:
            print(f"Blind write reg {reg} failed: {e}")

    def _recv_exact(self, size):
        data = bytearray()
        while len(data) < size:
            need = size - len(data)
            if self._rx_buffer:
                take = min(need, len(self._rx_buffer))
                data.extend(self._rx_buffer[:take])
                del self._rx_buffer[:take]
                continue
            chunk = self.tenso_scan.recv(need)
            if not chunk:
                raise ConnectionError("Socket closed while reading")
            data.extend(chunk)
        return data

    def _sync_header(self):
        header_bytes = self._recv_exact(2)
        while header_bytes != b"\xAA\xAA":
            header_bytes = header_bytes[1:] + self._recv_exact(1)
        return header_bytes

    @staticmethod
    def _channels_from_sample(unpacked_sample, active_mask):
        channels = [None, None, None, None]
        val_idx = 1
        for i in range(4):
            if active_mask & (1 << i):
                channels[i] = unpacked_sample[val_idx]
                val_idx += 1
        return channels

    def _receive_stream(self):
        header_format = "<HIHB"
        header_size = struct.calcsize(header_format)
        sample_n = 0

        while self.connected:
            try:
                full_header = self._sync_header() + self._recv_exact(header_size - 2)
                _, packet_id, active_mask, sample_count = struct.unpack(header_format, full_header)

                num_active = (active_mask & 0xF).bit_count()
                sample_size = 4 + num_active * 4
                payload = self._recv_exact(sample_count * sample_size)

                sample_format = "<I" + ("I" * num_active)
                offset = 0
                for _ in range(sample_count):
                    unpacked = struct.unpack(sample_format, payload[offset: offset + sample_size])
                    channels = self._channels_from_sample(unpacked, active_mask)
                    if self._csv_writer is not None:
                        self._csv_writer.writerow([packet_id, unpacked[0], *channels])

                    sample_n += 1
                    if sample_n % 100 == 0:
                        print(f"sample {sample_n}: pid={packet_id} ts={unpacked[0]} ch={channels}")

                    offset += sample_size

            except socket.timeout:
                continue
            except Exception as e:
                if self.connected:
                    print(f"[Stream] Error: {e}")
                return

    def _csv_filename(self):
        safe_ip = self.ip.replace(".", "_")
        name = f"tenzoscan_data_{safe_ip}.csv"
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
        self._csv_writer = csv.writer(self._csv_file)
        self._csv_writer.writerow(["Packet_ID", "Timestamp_us", "CH1", "CH2", "CH3", "CH4"])
        self._csv_file.flush()

    def _close_csv(self):
        if self._csv_file is not None:
            try:
                self._csv_file.flush()
                self._csv_file.close()
            except Exception as e:
                print(f"Error closing CSV: {e}")
            self._csv_file = None
            self._csv_writer = None

    def disconnect(self):
        was_connected = self.connected
        self.connected = False

        if self.tenso_scan is not None and was_connected:
            try:
                self.tenso_scan.settimeout(None)
                self.tenso_scan.setblocking(True)
                self._set_ram_register_blind(self.REG_MODE, self.AD_DISABLE)
                self._set_ram_register_blind(self.REG_STREAM_EN, 0)
            except Exception as e:
                print(f"Error stopping tenzoscan: {e}")

        if self._receive_thread is not None:
            self._receive_thread.join(timeout=2.0)
            self._receive_thread = None

        if self.tenso_scan is not None:
            try:
                self.tenso_scan.close()
            except Exception as e:
                print(f"Error closing tenzoscan socket: {e}")
            self.tenso_scan = None

        self._rx_buffer.clear()
        self._close_csv()


if __name__ == "__main__":
    controller = TensoScannerController()
    try:
        controller.start()
        input("\nStreaming... Press ENTER to stop.\n")
    except KeyboardInterrupt:
        print("\nStopping tenzoscan...")
    finally:
        controller.disconnect()
        controller.wait(3000)
