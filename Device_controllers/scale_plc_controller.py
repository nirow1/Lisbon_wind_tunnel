from PySide6.QtCore import Signal
from Device_controllers.polling_plc_controller import PollingPLCController
from Utils.helper_functions import byte_to_bits


class ScalePLCController(PollingPLCController):
    SCALE_DATA = Signal(dict)
    STATUS_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.10.12"):
        super().__init__(ip_address, read_nb=2, write_nb=3, param_nb=4)


    def _read_main_data(self) -> dict | None:
        try:
            scale_data = self._read_plc_data(self.read_nb, 0, 34, '>4dH')

            tats_data = byte_to_bits(((scale_data[4] & 0xFF) << 8) | (scale_data[4] >> 8), "little")

            return [{"roll": scale_data[2], "pitch": scale_data[1], "yaw": scale_data[0], "axis_4": scale_data[3]},
                    {"ready": scale_data[3], "moving": scale_data[4]}]

        except Exception as e:
            print(e)
            return None

    def _emit_read_data(self, data) -> None:
        self.SCALE_DATA.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def set_pitch_yaw_roll(self, pitch: float, yaw: float, roll: float) -> None:
        self._write_plc_float(self.write_nb, 4, pitch)
        self._write_plc_float(self.write_nb, 8, yaw)
        self._write_plc_float(self.write_nb, 12, roll)
        self.start_driver()
    
    def set_pitch_yaw_roll(self, pitch: float, yaw: float, roll: float) -> None:
        self.set_yaw(yaw)
        self.set_pitch(pitch)
        self.set_roll(roll)
        self.start_driver()

    def set_yaw(self, yaw: float):
        self._write_element(2, yaw)

    def set_pitch(self, pitch: float):
        self._write_element(6, pitch)

    def set_roll(self, roll: float):
        self._write_element(10, roll)
