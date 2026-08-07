import time
from threading import Thread
from PySide6.QtCore import Signal
from Device_controllers.plc_controller import PLCController
from Utils.helper_functions import control_dict_to_bytes


class DriverPLCController(PLCController):
    DRIVERS_POS = Signal(dict)

    def __init__(self, ip_address="192.168.10.2"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=102)
        self.PLC_CONNECTED.connect(self._start_reading_plc_data)
        self.control_byte = { "block": 0, "start": 0, "stop": 0, "confirm": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0}
        self.status_byte = { "ready": 0, "error": 0, "moving": 0, "estop_active": 0, "xHWLimit": 0, "xSWLimit": 0, "6": 0, "x_homed": 0, "y_homed": 0, "z_homed": 0, "all_homed": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0}

    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        while self.connected:
            try:
                main_data_dict = self._read_main_data()
                self.DRIVERS_POS.emit(main_data_dict)
            except Exception as e:
                main_data_dict = {}
                print(e)

            time.sleep(0.1)

    # todo: there might be movement indicator for all axes, in that case traverser_view could be simplified. Need to be confirmed.
    def _read_main_data(self) -> dict | None:
        try:
            position_data = self._read_plc_data(self.read_nb, 0, 24, '>3d')

            return {"x": position_data[0], "y": position_data[1], "z": position_data[2]}

        except Exception as e:
            print(e)
            self._stop_timers()
            return None

    def start_driver(self):
        self.control_byte["start"] = 1
        data_short = control_dict_to_bytes(self.control_byte, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)

    def stop_driver(self):
        self.control_byte["stop"] = 1
        data_short = control_dict_to_bytes(self.control_byte, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)

    def confirm_error(self):
        self.control_byte["confirm"] = 1
        data_short = control_dict_to_bytes(self.control_byte, endian="little")
        self._write_plc_data(self.write_nb, 0, 2,  data_short)

    def set_2d_pos(self, x: int, y: int):
        self.set_2d_x(x)
        self.set_2d_y(y)
        self.start_driver()

    def set_3d_pos(self, x: int, y: int, z: int):
        self.set_3d_x(x)
        self.set_3d_y(y)
        self.set_3d_z(z)
        self.start_driver()

    def set_2d_x(self, x: int):
        self.write_plc_data(self.write_nb, 2, x)

    def set_2d_y(self, y: int):
        self.write_plc_data(self.write_nb, 6, y)

    def set_3d_x(self, x: int):
        self.write_plc_data(self.write_nb, 10, x)

    def set_3d_y(self, y: int):
        self.write_plc_data(self.write_nb, 2, x)

    def set_3d_z(self, z: int):
        self.write_plc_data(self.write_nb, 6, y)