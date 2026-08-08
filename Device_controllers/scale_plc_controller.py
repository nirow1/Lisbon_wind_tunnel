from PySide6.QtCore import Signal
from Device_controllers.polling_plc_controller import PollingPLCController


class ScalePLCController(PollingPLCController):
    SCALE_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.10.12"):
        super().__init__(ip_address, read_nb=2, write_nb=3, param_nb=4)

    # todo: missing equations and pitch yaw roll setters
    def _read_main_data(self) -> dict | None:
        try:
            b1 = self._read_plc_data(self.read_nb, 4, 40, '>40B')

            return {key: value for key, value in enumerate(b1)}

        except Exception as e:
            print(e)
            self._stop_timers()
            return None

    def _emit_read_data(self, data):
        self.SCALE_DATA.emit(data)
