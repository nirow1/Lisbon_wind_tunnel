import time
from threading import Thread
from time import sleep
from turtledemo.penrose import start

from PySide6.QtCore import Signal
from Device_controllers.plc_controller import PLCController
from Utils.helper_functions import control_dict_to_bytes, byte_to_bits


class DriverPLCController(PLCController):
    DRIVERS_POS = Signal(dict)
    STATUS_DATA = Signal(dict)

    #10 = 2d, 12 = vahy
    def __init__(self, ip_address="192.168.10.11"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=102)
        self.control_byte = {"block": 0, "start": 0, "stop": 0, "confirm": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0}
        self.control_byte_map = {"block": 0, "start": 1, "stop": 2, "confirm": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                             "9": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15}
        self.status_byte = { "ready": 0, "error": 0, "moving": 0, "estop_active": 0, "xHWLimit": 0, "xSWLimit": 0, "6": 0, "x_homed": 0, "y_homed": 0, "z_homed": 0, "all_homed": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0}
        self.PLC_CONNECTED.connect(self._start_reading_plc_data)
,
    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        while self.connected:
            try:
                main_data_dict = self._read_main_data()
                if main_data_dict is None:
                    self.connected = False
                    self.PLC_CONNECTED.emit(False)
                    break

                self.DRIVERS_POS.emit(main_data_dict[0])
                self.STATUS_DATA.emit(main_data_dict[1])
            except Exception as e:
                main_data_dict = {}
                print(e)

            time.sleep(0.1)

    def _read_main_data(self) -> list[dict] | None:
        try:
            position_data = self._read_plc_data(self.read_nb, 0, 34, '>3d8BH')

            stats_data = byte_to_bits(((position_data[11] & 0xFF) << 8) | (position_data[11] >> 8), "little")
            return [{"x": position_data[0], "y": position_data[1], "z": position_data[2]},
                    { "ready": stats_data[0], "moving": stats_data[1]}]

        except Exception as e:
            print(e)
            return None

    def start_driver(self):
        self.control_byte["start"] = 1
        data_short = control_dict_to_bytes(self.control_byte, self.control_byte_map, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)
        sleep(1)
        self.control_byte["start"] = 0
        self._write_plc_data(self.write_nb, 0, 2, data_short)

    def stop_driver(self):
        self.control_byte["stop"] = 1
        data_short = control_dict_to_bytes(self.control_byte, self.control_byte_map, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)

    def confirm_error(self):
        self.control_byte["confirm"] = 1
        data_short = control_dict_to_bytes(self.control_byte, self.control_byte_map, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)

    def set_2d_pos(self, x: float, y: float):
        self.set_2d_x(x)
        self.set_2d_y(y)
        self.start_driver()

    def set_3d_pos(self, x: float, y: float, z: float):
        self.set_3d_x(x)
        self.set_3d_y(y)
        self.set_3d_z(z)
        self.start_driver()

    def set_2d_x(self, x: float):
        self._write_plc_float(self.write_nb, 2, x)

    def set_2d_y(self, y: float):
        self._write_plc_float(self.write_nb, 6, y)

    def set_3d_x(self, x: float):
        self._write_plc_float(self.write_nb, 2, x)

    def set_3d_y(self, y: float):
        self._write_plc_float(self.write_nb, 6, y)

    def set_3d_z(self, z: float):
        self._write_plc_float(self.write_nb, 10, z)