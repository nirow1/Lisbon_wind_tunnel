from threading import Thread
from time import sleep

from Device_controllers.plc_controller import PLCController
from Utils.helper_functions import control_dict_to_bytes


class PollingPLCController(PLCController):
    def __init__(self, ip, read_nb, write_nb, param_nb):
        super().__init__(ip, read_nb, write_nb, param_nb)
        self.control_byte = {
            "block": 0, "start": 0, "stop": 0, "confirm": 0, "4": 0, "5": 0, "6": 0, "7": 0,
            "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0,
        }
        self.control_byte_map = {
            "block": 0, "start": 1, "stop": 2, "confirm": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15,
        }
        self.status_byte = {
            "ready": 0, "error": 0, "moving": 0, "estop_active": 0, "xHWLimit": 0, "xSWLimit": 0,
            "6": 0, "x_homed": 0, "y_homed": 0, "z_homed": 0, "all_homed": 0, "11": 0, "12": 0,
            "13": 0, "14": 0, "15": 0,
        }
        self.PLC_CONNECTED.connect(self._start_reading_plc_data)

    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        while self.connected:
            try:
                data = self._read_main_data()
                if data is None:
                    self.connected = False
                    self.PLC_CONNECTED.emit(False)
                    break
                self._emit_read_data(data)
            except Exception as e:
                print(e)

            sleep(0.1)

    def _read_main_data(self):
        raise NotImplementedError

    def _emit_read_data(self, data):
        raise NotImplementedError

    def _write_element(self, offset: int, value: float):
        self._write_plc_float(self.write_nb, offset, value)

    def start_driver(self):
        Thread(target=self.send_ping, args=["start"], daemon=True).start()

    def stop_driver(self):
        Thread(target=self.send_ping, args=["stop"], daemon=True).start()

    def confirm_error(self):
        Thread(target=self.send_ping, args=["confirm"], daemon=True).start()

    def send_ping(self, key: str):
        self.send_control_byte(key, 1)
        sleep(0.1)
        self.send_control_byte(key, 0)

    def send_control_byte(self, key: str, value: int):
        self.control_byte[key] = value
        data_short = control_dict_to_bytes(self.control_byte, self.control_byte_map, endian="little")
        self._write_plc_data(self.write_nb, 0, 2, data_short)
