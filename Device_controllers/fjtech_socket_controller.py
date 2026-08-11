import socket
import time
from typing import ClassVar

from PySide6.QtCore import QThread

from Utils.device_csv_logger import DeviceCsvLogger


class SocketDeviceController(QThread):
    """Shared TCP:23 + AT+RAM_RW + CSV lifecycle for FJTech socket devices."""

    _csv_basename = "device_data"
    _csv_header: ClassVar[list[str]] = []
    _csv_delimiter = ","

    def __init__(self, ip: str, port: int = 23):
        super().__init__()
        self.ip = ip
        self.port = port
        self.connected = False
        self._sock: socket.socket | None = None
        self._worker_thread = None
        self._csv = DeviceCsvLogger(
            basename=self._csv_basename,
            header=self._csv_header,
            delimiter=self._csv_delimiter,
            ip=self.ip,
        )

    def set_csv_path(self, path):
        self._csv.set_directory(path if path else "")

    def start_csv_logging(self):
        self._csv.start()

    def stop_csv_logging(self):
        self._csv.stop()

    def _write_csv_row(self, row):
        self._csv.write_row(row)

    def _connect_socket(self, timeout: float | None = None) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if timeout is not None:
                sock.settimeout(timeout)
            sock.connect((self.ip, self.port))
            self._sock = sock
            self.connected = True
            return True
        except Exception as e:
            print(f"Failed to connect to {self.ip}:{self.port}: {e}")
            self._sock = None
            self.connected = False
            return False

    def _set_ram_register_blind(self, reg, value):
        """Blind write for safe shutdown without waiting for a reply."""
        if self._sock is None:
            return
        try:
            cmd = f"AT+RAM_RW={reg},1\r\n".encode("ascii")
            self._sock.sendall(cmd)
            time.sleep(0.05)
            self._sock.sendall(bytes([value]))
            time.sleep(0.05)
        except Exception as e:
            print(f"Blind write reg {reg} failed: {e}")

    def _close_socket(self):
        if self._sock is not None:
            try:
                self._sock.close()
            except Exception as e:
                print(f"Error closing socket {self.ip}: {e}")
            self._sock = None

    def _join_worker_thread(self, timeout: float | None = 2.0):
        if self._worker_thread is not None:
            self._worker_thread.join(timeout=timeout)
            self._worker_thread = None

    def _on_disconnect(self):
        """Subclass hook: stop measurement on the device before closing the socket."""

    def disconnect(self):
        self.connected = False
        try:
            if self._sock is not None:
                try:
                    self._sock.settimeout(None)
                    self._sock.setblocking(True)
                except Exception:
                    pass
                self._on_disconnect()
        except Exception as e:
            print(f"Error stopping device {self.ip}: {e}")

        self._join_worker_thread()
        self._close_socket()
        self.stop_csv_logging()
