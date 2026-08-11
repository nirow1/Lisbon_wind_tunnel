import struct
import threading
import time

from PySide6.QtCore import Signal

from Device_controllers.fjtech_socket_controller import SocketDeviceController


class TensoScannerController(SocketDeviceController):
    TENSO_DATA = Signal(list)

    _csv_basename = "tenzoscan_data"
    _csv_delimiter = ","
    _csv_header = ["Packet_ID", "Timestamp_us", "CH1", "CH2", "CH3"]

    def __init__(self, ip="192.168.10.96"):
        super().__init__(ip)
        self._rx_buffer = bytearray()

    def run(self):
        while not self.connected:
            if self._connect():
                self._start_streaming()
                self._join_worker_thread(timeout=None)
                return
            time.sleep(2)

    def _connect(self):
        if not self._connect_socket(timeout=2.0):
            return False
        self._rx_buffer.clear()
        # Previous sessions may leave the device streaming; stop and clear the socket.
        self._set_ram_register_blind(8, 0)   # mode = disable
        self._set_ram_register_blind(18, 0)  # stream enable = off
        self._drain_socket()
        return True

    def _drain_socket(self):
        if self._sock is None:
            return
        self._rx_buffer.clear()
        prev_timeout = self._sock.gettimeout()
        self._sock.settimeout(0.05)
        try:
            while True:
                chunk = self._sock.recv(4096)
                if not chunk:
                    break
        except TimeoutError:
            pass
        except OSError:
            pass
        finally:
            self._sock.settimeout(prev_timeout if prev_timeout is not None else 2.0)

    def _start_streaming(self):
        try:
            # Complete both AT writes before the reader thread touches the socket.
            # send_ram_write keeps any trailing 0xAA payload in _rx_buffer.
            self.send_ram_write(18, 1)  # stream enable
            self.send_ram_write(8, 1)   # mode = max speed
            self._worker_thread = threading.Thread(target=self._receive_stream, daemon=True)
            self._worker_thread.start()
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
            chunk = self._sock.recv(1024)
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
        self._sock.sendall(cmd.encode("ascii"))
        self._recv_at_response(b"Waiting")
        self._sock.sendall(bytes([value]))
        self._recv_at_response(b"OK")

    def _recv_exact(self, size):
        data = bytearray()
        while len(data) < size:
            need = size - len(data)
            if self._rx_buffer:
                take = min(need, len(self._rx_buffer))
                data.extend(self._rx_buffer[:take])
                del self._rx_buffer[:take]
                continue
            chunk = self._sock.recv(need)
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
                    self._write_csv_row([packet_id, unpacked[0], *channels[:3]])
                    sample_n += 1
                    if sample_n % 100 == 0:
                        self.TENSO_DATA.emit(channels[:3])

                    offset += sample_size

            except TimeoutError:
                continue
            except Exception as e:
                if self.connected:
                    print(f"[Stream] Error: {e}")
                return

    def _on_disconnect(self):
        self._set_ram_register_blind(8, 0)   # mode = disable
        self._set_ram_register_blind(18, 0)  # stream enable = off

    def disconnect(self):
        super().disconnect()
        self._rx_buffer.clear()


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
