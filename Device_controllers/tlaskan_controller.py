import sys
import threading
import time
from struct import unpack

from PySide6.QtCore import Signal

from Device_controllers.fjtech_socket_controller import SocketDeviceController


class TlaskanController(SocketDeviceController):
    PRESSURE_DATA = Signal(list)
    DEVICE_CONNECTED = Signal(bool)

    _csv_basename = "tlaskan_data"
    _csv_delimiter = ";"
    _csv_header = (
        ["Timestamp_ms", "Packet_ID"]
        + [item for i in range(12) for item in (f"S{i}_Press", f"S{i}_Status")]
    )

    def __init__(self, ip="192.168.10.98"):
        super().__init__(ip)
        self.zero_values = [0.0 for _ in range(12)]
        self.processed_pressure = []
        self._running = False

    def _print_data_line(self, data):
        """Always rewrite console line 1; leave the cursor where it was."""
        text = " | ".join(f"{v:7.3f}" for v in data)
        # save cursor, go to (1,1), clear line, print, restore cursor
        sys.stdout.write(
            f"\033[s\033[1;1H\033[2KTLASKAN [{self.ip}]: {text}\033[u"
        )
        sys.stdout.flush()

    def run(self):
        self._running = True
        self._connect_to_tlaskan()

    def _connect_to_tlaskan(self):
        for _ in range(3):
            if not self._running:
                return
            if self._connect_socket():
                self.DEVICE_CONNECTED.emit(True)
                self._sock.send(b"AT+RAM_RW=5,1\x0d\x0a")
                self._sock.send(b"\x01")
                self._start_communication()
                return
            time.sleep(2)
        self._running = False
        self.DEVICE_CONNECTED.emit(False)

    def _start_communication(self):
        self._worker_thread = threading.Thread(target=self._send_measure_request, daemon=True)
        self._worker_thread.start()
        self._listen_to_tls()

    def _mark_disconnected(self):
        """Emit once when the socket is no longer usable (peer gone / I/O failed)."""
        if not self.connected:
            return
        self.connected = False
        self.DEVICE_CONNECTED.emit(False)

    def _send_measure_request(self):
        while self.connected:
            time.sleep(0.1)
            try:
                self._sock.send(b"AT+RAM_RW=6,72,BIN,?\x0d\x0a")
            except OSError:
                self._mark_disconnected()
                break

    def _listen_to_tls(self):
        emit_counter = 0
        try:
            self._sock.recv(1024)
        except OSError:
            self._mark_disconnected()
            return
        while self.connected:
            try:
                msg = self._sock.recv(1024)
                if not msg:
                    # Peer closed the TCP connection — fastest reliable disconnect signal
                    self._mark_disconnected()
                    break
                payload = msg[22:94]
                if len(payload) != 72:
                    continue

                tlaskan_data = unpack("=" + "BfB" * 12, payload)
                timestamp_ms = int(time.time() * 1000)
                row = [timestamp_ms, 0]
                pressures = []
                for i in range(12):
                    base = i * 3
                    press = float(tlaskan_data[base + 1]) * 249.089
                    status = tlaskan_data[base + 2]
                    row.extend([f"{press:.4f}", status])
                    pressures.append(press)
                self._write_csv_row(row)
                self.processed_pressure = [
                    round(pressures[i], 3) - self.zero_values[i]
                    for i in range(len(pressures))
                ]
                self._print_data_line(self.processed_pressure)
                emit_counter += 1
                if emit_counter % 10 == 0:
                    self.PRESSURE_DATA.emit(self.processed_pressure)
            except TimeoutError:
                continue
            except OSError:
                self._mark_disconnected()
                break

    def _on_disconnect(self):
        self._set_ram_register_blind(5, 0)

    def disconnect(self):
        was_connected = self.connected
        self._running = False
        super().disconnect()
        if was_connected:
            self.DEVICE_CONNECTED.emit(False)
        self.wait(3000)

    def set_zero_values(self):
        if not self.connected or len(self.processed_pressure) != len(self.zero_values):
            return
        self.zero_values = [
            self.zero_values[i] + self.processed_pressure[i]
            for i in range(len(self.zero_values))
        ]


if __name__ == "__main__":
    tls = TlaskanController()
    try:
        tls.run()
    except KeyboardInterrupt:
        print("\nStopping TLASKAN...")
    finally:
        tls.disconnect()
        print("TLASKAN connection closed.")
