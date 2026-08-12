from PySide6.QtCore import Signal

from Device_controllers.polling_plc_controller import PollingPLCController
from Utils.helper_functions import byte_to_bits


class Driver2DPLCController(PollingPLCController):
    DRIVERS_POS = Signal(dict)
    STATUS_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.10.10"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=102)

    def _read_main_data(self) -> list[dict] | None:
        try:
            position_data = self._read_plc_data(self.read_nb, 0, 26, '>2d8BH')
            if position_data is None:
                raise Exception("No position data received")

            stats_data = byte_to_bits(((position_data[10] & 0xFF) << 8) | (position_data[10] >> 8), "little")
            return [{"x": position_data[0], "y": position_data[1]},
                    {"ready": stats_data[0], "moving": stats_data[2]}]

        except Exception as e:
            print(e)
            return None

    def _emit_read_data(self, data):
        self.DRIVERS_POS.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def set_2d_pos(self, x: float, y: float):
        self.set_2d_x(x)
        self.set_2d_y(y)
        self.start_driver()

    def set_2d_x(self, x: float):
        self._write_element(2, x)

    def set_2d_y(self, y: float):
        self._write_element(6, y)
