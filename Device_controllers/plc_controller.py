import struct
import time

from snap7 import client, util
from PySide6.QtCore import QThread, Signal, QTimer
from threading import Lock, Thread
from time import sleep
from Utils.helper_functions import list_to_ushort


class PLCController(QThread):
    PLC_DATA = Signal(dict)
    STATUS_DATA = Signal(dict)
    PLC_CONNECTED = Signal(bool)
    CONTROL_BYTE = Signal(dict)
    PARAM_DATA_FAN = Signal(dict)
    PARAM_DATA_STATUS = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.2.1"
        self.read_nb = 2
        self.write_nb = 3
        self.param_nb = 8
        self.vfd = bytearray(b'\x05')
        self.connected = False
        self.sending = False
        self.control_byte = {"start": 0, "stop": 0, "ack": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0,
                             "pump": 0, "cooling": 0, "PID": 0, "control": 0, "12": 0, "13": 0, "14": 0, "15": 0}

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
                self._start_reading_plc_data()
                break
            except Exception as e:
                print(e)
                sleep(5)

    # -------- Read functions ---------
    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        count = 1
        while self.connected:
            try:
                main_data_dict = self._read_main_data()
            except Exception as e:
                main_data_dict = {}
                print(e)

            print(f"{count}: {main_data_dict}")

            count += 1
            time.sleep(0.1)

    def _read_main_data(self) -> dict | None:
        try:
            b1 = self._read_plc_data(self.read_nb,4, 40, '>40B')

            return {key:value for key, value in enumerate(b1)}

        except Exception as e:
            print(e)
            self._stop_timers()
            return None

    # -------- Write functions ---------
    def _start_watchdog(self):
        self._watchdog_timer = QTimer()  # instance proměnná, ne lokální!
        self._watchdog_timer.setInterval(1000)
        self._watchdog_timer.timeout.connect(self._ping_watchdog)
        self._watchdog_timer.start()

    def _ping_watchdog(self):
        try:
            code = self._read_plc_data(self.read_nb, 0, 2)
            self._write_plc_ushort(0, code[0])
        except Exception as e:
            print(e)
            self._stop_timers()

    def set_engine_frequency(self, request: float):
        self._write_plc_float(4, request)

    def set_wind_velocity(self, velocity: float):
        self._write_plc_float(8, velocity)

    def set_ramp_down(self, value: int):
        self._write_plc_int(50, value)

    def set_ramp_up(self, value: int):
        self._write_plc_int(48, value)

    def set_run_dur(self, value: int):
        self._write_plc_int(52, value)

    def set_pid(self, kp: float, ti: float, td: float):
        self._write_plc_float(2, kp, param=True)
        self._write_plc_float(6, ti, param=True)
        self._write_plc_float(10, td, param=True)

    def switch_pid(self, state: bool):
        self.control_byte["PID"] = state

    def switch_pump(self, state: bool):
        self._switch_bit("pump", state)

    def switch_cooling(self, state: bool):
        self._switch_bit("cooling", state)

    def switch_control(self, state: bool):
        self.control_byte["control"] = state

    def start_engine(self):
        self.control_byte["start"] = 1
        self.control_byte["stop"] = 0
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_ushort(2, data_short)
        cb = self._read_control_byte()

    def read_parameter_data(self) -> tuple | None:
        return self._read_plc_data(self.param_nb, 0, 114, '>h4fxB7f3h2B9fhf8h')

    def stop_engine(self):
        self.control_byte["stop"] = 1
        self.control_byte["start"] = 0
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_ushort(2, data_short)

    # -------- Helper functions ---------

    def _write_plc_int(self, pos: int, request: int):
        if not self.connected:
            return None

        with self._lock:
            try:
                buffer = bytearray(2)          # 4 byty
                util.set_int(buffer, 0, request)  # zapíše float do bufferu na offset 0
                self.plc.db_write(self.param_nb, pos, buffer)
            except Exception as e:
                print(f"[ERROR] _write_plc_int: {e}")

    def _write_plc_float(self, pos: int, request: float, param: bool = False):
        if not self.connected:
            return None

        with self._lock:
            try:
                buffer = bytearray(4)          # REAL = 4 byty
                util.set_real(buffer, 0, request)  # zapíše float do bufferu na offset 0
                self.plc.db_write(self.write_nb if not param else self.param_nb, pos, buffer)
            except Exception as e:
                print(f"[ERROR] _write_plc_float: {e}")

    def _write_plc_ushort(self, pos: int, request: int):
        if not self.connected:
            return None

        with self._lock:
            try:
                ushort_in_bytes = struct.pack('>H', request)
                self.plc.db_write(self.write_nb, pos, bytearray(ushort_in_bytes))
            except Exception as e:
                print(f"[ERROR] write_logo_ushort: {e}")

    def _switch_bit(self, attribute: str, state: bool):
        self.control_byte[attribute] = state
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_ushort(2, data_short)

    def _read_control_byte(self) -> dict:
        data = self._read_plc_data(self.read_nb, 2, 2, '>H')
        if data is None:
            return {}
        value = data[0]
        keys = list(self.control_byte.keys())
        return {key: (value >> i) & 1 for i, key in enumerate(keys)}

    def _write_plc_byte(self, pos: int, request: bytearray):
        if not self.connected:
            return None

        with self._lock:
            try:
                self.plc.db_write(self.write_nb, pos, request)
            except Exception as e:
                print(f"[ERROR] write_logo_ushort: {e}")

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

    @staticmethod
    def byte_to_bits(byte):
        return [(byte >> i) & 1 for i in range(7, -1, -1)]

    def disconnect(self):
        try:
            self.connected = False
            self._write_plc_ushort(4, 0)  # stop engine
            self.stop_engine()
            self.plc.disconnect()
            self.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    plc = PLCController()
    plc.run()
