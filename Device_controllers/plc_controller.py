import struct
from threading import Lock
from time import sleep

from PySide6.QtCore import QThread, QTimer, Signal
from snap7 import client, util


class PLCController(QThread):
    PLC_CONNECTED = Signal(bool)

    def __init__(self, ip, read_nb, write_nb, param_nb):
        super().__init__()
        self.ip = ip
        self.read_nb = read_nb
        self.write_nb = write_nb
        self.param_nb = param_nb
        self.connected = False
        self._active = False
        self.sending = False

        self._watchdog_timer = QTimer()
        self.watchdog_count = 0

        self.averaging_window = []

        self._lock = Lock()

    def run(self):
        self._active = True
        self._connect_to_plc()
        # Only run the event loop if this session is still active and connected.
        # Avoids staying alive / reconnecting after disconnect during connect.
        if self._active and self.connected:
            self.exec()

    def _connect_to_plc(self):
        while self._active and not self.connected:
            try:
                self.plc = client.Client()
                self.plc.connect(self.ip, 0, 1)
                if not self._active:
                    try:
                        self.plc.disconnect()
                    except Exception:
                        pass
                    return
                self.connected = self.plc.get_connected()
                self.PLC_CONNECTED.emit(self.connected)
                break
            except Exception as e:
                print(e)
                # Interruptible backoff so disconnect does not wait a full 5s
                for _ in range(50):
                    if not self._active:
                        return
                    sleep(0.1)

    # -------- Write functions ---------
    def _start_watchdog(self):
        self._watchdog_timer.setInterval(1000)
        self._watchdog_timer.timeout.connect(self._ping_watchdog)
        self._watchdog_timer.start()

    def _ping_watchdog(self):
        try:
            self._write_plc_int(self.write_nb, 0, self.watchdog_count)
        except Exception as e:
            print(e)
            self._stop_timers()

    # -------- Helper functions ---------

    def _write_plc_int(self, db: int, pos: int, request: int):
        self._write_plc_data(db, pos, 2, request)

    def _write_plc_float(self,db: int, pos: int, request: float):
        self._write_plc_data(db, pos, 4, request)

    def _write_plc_data(self, db: int, pos: int, size: int, request: bytes | float):
        if not self.connected:
            return

        with self._lock:
            try:
                # INT (2 bytes)
                if isinstance(request, int):
                    buffer = bytearray(2)
                    util.set_int(buffer, 0, request)

                # FLOAT (4 bytes)
                elif isinstance(request, float):
                    buffer = bytearray(4)
                    util.set_real(buffer, 0, request)

                # BYTES / BYTEARRAY
                elif isinstance(request, (bytes, bytearray)):
                    if len(request) != size:
                        raise ValueError(f"Byte request length {len(request)} != size {size}")
                    buffer = bytearray(request)  # copy

                else:
                    raise TypeError(f"Unsupported PLC write type: {type(request)}")

                self.plc.db_write(db, pos, buffer)

            except Exception as e:
                print(f"[ERROR] _write_plc_data: {e}")

    def _write_plc_bool_byte(self, db: int, offset: int, state: int):
        """Write a single-bit boolean as a full byte (only bit 0 used)."""
        with self._lock:
            self.plc.db_write(db, offset, bytearray([1 if state else 0]))

    def _write_plc_bits(self, db: int, offset: int, bit_states: dict):
        """Read-modify-write multiple bits in a single byte. bit_states: {bit_index: 0|1}"""
        with self._lock:
            byte_val = self.plc.db_read(db, offset, 1)[0]
        for bit, state in bit_states.items():
            if state:
                byte_val |= (1 << bit)
            else:
                byte_val &= ~(1 << bit)
        with self._lock:
            self.plc.db_write(db, offset, bytearray([byte_val]))

    def _read_plc_data(self, db:int,  pos: int, size: int, frm: str = '>H'):
        if not self.connected:
            return None

        with self._lock:
            try:
                msg = self.plc.db_read(db, pos, size)
                return struct.unpack(frm, msg)
            except Exception as e:
                print(f"[ERROR] _read_plc_data: {e}")
                return None

    def _stop_timers(self):
        self._watchdog_timer.stop()

    def disconnect(self):
        was_connected = self.connected
        self._active = False
        self.connected = False
        try:
            self._stop_timers()
        except Exception:
            pass
        try:
            if getattr(self, "plc", None) is not None:
                self.plc.disconnect()
        except Exception as e:
            print(e)
        if was_connected:
            self.PLC_CONNECTED.emit(False)
        self.quit()
        self.wait(3000)

    @staticmethod
    def byte_to_bits(byte):
        return [(byte >> i) & 1 for i in range(7, -1, -1)]