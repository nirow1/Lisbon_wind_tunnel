from threading import Thread
from time import sleep

from PySide6.QtCore import Signal

from Device_controllers.polling_plc_controller import PollingPLCController
from Utils.helper_functions import byte_to_bits


class Driver3DPLCController(PollingPLCController):
    DRIVERS_POS = Signal(dict)
    STATUS_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.10.11"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=102)
        self._is_all_homed: bool | None = None
        self.PLC_CONNECTED.connect(self._on_plc_connected)

    def _read_main_data(self) -> list[dict] | None:
        try:
            position_data = self._read_plc_data(self.read_nb, 0, 34, '>3d8BH')

            stats_data = byte_to_bits(((position_data[11] & 0xFF) << 8) | (position_data[11] >> 8), "little")
            self._is_all_homed = bool(stats_data[10])
            return [{"x": position_data[0], "y": position_data[1], "z": position_data[2]},
                    {"ready": stats_data[0], "moving": stats_data[2], "allhoomed": stats_data[10]}]

        except Exception as e:
            print(e)
            return None

    def _on_plc_connected(self, connected: bool = True) -> None:
        if not connected:
            self._is_all_homed = None
            return
        self._is_all_homed = None
        Thread(target=self._home_after_status, daemon=True).start()

    def _home_after_status(self) -> None:
        while self.connected and self._is_all_homed is None:
            sleep(0.05)
        if self.connected and not self._is_all_homed:
            self.home_driver()

    def _emit_read_data(self, data):
        self.DRIVERS_POS.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def home_driver(self):
        super().home_driver(18)

    def set_3d_pos(self, x: float, y: float, z: float):
        self.set_3d_x(x)
        self.set_3d_y(y)
        self.set_3d_z(z)
        self.start_driver()

    def set_3d_x(self, x: float):
        self._write_element(2, x)

    def set_3d_y(self, y: float):
        self._write_element(6, y)

    def set_3d_z(self, z: float):
        self._write_element(10, z)
