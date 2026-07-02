import struct

from snap7 import client, util
from PySide6.QtCore import QThread, Signal, QTimer
from threading import Lock
from time import sleep


class PLCController(QThread):
    PLC_CONNECTED = Signal(bool)

    def __init__(self, ip, read_nb, write_nb, param_nb):
        super().__init__()
        self.ip = ip
        self.read_nb = read_nb
        self.write_nb = write_nb
        self.param_nb = param_nb
        self.connected = False
        self.sending = False

        self.averaging_window = []

        self._lock = Lock()

    def run(self):
        self._connect_to_plc()
        self.exec()  # Qt event loop → QTimer funguje

    def _connect_to_plc(self):
        while not self.connected:
            try:
                self.plc = client.Client()
                self.plc.connect(self.ip, 0, 1)
                self.connected = self.plc.get_connected()
                self.PLC_CONNECTED.emit(self.connected)
                break
            except Exception as e:
                print(e)
                sleep(5)

    # -------- Write functions ---------
    def _start_watchdog(self):
        self._watchdog_timer = QTimer()  # instance proměnná, ne lokální!
        self._watchdog_timer.setInterval(1000)
        self._watchdog_timer.timeout.connect(self._ping_watchdog)
        self._watchdog_timer.start()

    def _ping_watchdog(self):
        try:
            code = self._read_plc_data(self.read_nb, 0, 2)
            self._write_plc_int(self.write_nb, 0, code[0])
        except Exception as e:
            print(e)
            self._stop_timers()

    # -------- Helper functions ---------

    def _write_plc_int(self, db: int, pos: int, request: int):
        self._write_plc_data(db, pos, 2, request)

    def _write_plc_float(self,db: int, pos: int, request: float):
        self._write_plc_data(db, pos, 4, request)

    def _write_plc_data(self, db: int, pos: int, size: int, request: bytes|int|float):
        if not self.connected:
            return None

        with self._lock:
            try:
                # INT (2 bytes)
                if isinstance(request, int):
                    if size != 2:
                        raise ValueError("INT requires size=2")
                    buffer = bytearray(2)
                    util.set_int(buffer, 0, request)

                # FLOAT (4 bytes)
                elif isinstance(request, float):
                    if size != 4:
                        raise ValueError("FLOAT requires size=4")
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
        try:
            self.connected = False
            self.plc.disconnect()
            self.quit()
        except Exception as e:
            print(e)

    @staticmethod
    def byte_to_bits(byte):
        return [(byte >> i) & 1 for i in range(7, -1, -1)]


if __name__ == '__main__':
    plc = PLCController()
    plc.run()
