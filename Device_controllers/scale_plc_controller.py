from PySide6.QtCore import Signal

from Device_controllers.polling_plc_controller import PollingPLCController
from Device_controllers.tenso_scanner_controller import TensoScannerController
from Utils.helper_functions import byte_to_bits


class ScalePLCController(PollingPLCController):
    SCALE_DATA = Signal(dict)
    POS_DATA = Signal(dict)
    STATUS_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.10.12"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=4)
        self.tenso_scanners = (TensoScannerController("192.168.10.96"),
                               TensoScannerController("192.168.10.97"))
        self.tenso_data = {"ch1_tso1": 0, "ch2_tso1": 0, "ch3_tso1": 0,
                           "ch1_tso2": 0, "ch2_tso2": 0, "ch3_tso2": 0,}
        # TEMP: collect samples for column averages
        self._tenso_samples: list[list] = []
        self.bind_emits()

    def _read_main_data(self) -> list | None:
        try:
            scale_data = self._read_plc_data(self.read_nb, 0, 34, '>4dH')

            status_data = byte_to_bits(((scale_data[4] & 0xFF) << 8) | (scale_data[4] >> 8), "little")

            return [{"roll": scale_data[2], "pitch": scale_data[1], "yaw": scale_data[0], "axis_4": scale_data[3]},
                    {"ready": status_data[0], "moving": status_data[1]}]

        except Exception as e:
            print(e)
            return None

    def bind_emits(self) -> None:
        self.tenso_scanners[0].TENSO_DATA.connect(lambda data: self._handle_tenso_data(data, 1))
        self.tenso_scanners[1].TENSO_DATA.connect(lambda data: self._handle_tenso_data(data, 2))
        self.PLC_CONNECTED.connect(self.connect_to_tenso_scanners)

    def connect_to_tenso_scanners(self, connected: bool = True) -> None:
        if not connected:
            return
        self.tenso_scanners[0].start()
        self.tenso_scanners[1].start()

    def _handle_tenso_data(self, data: list, id: int) -> None:
        if id == 1:
            self.tenso_data["ch1_tso1"] = data[0]
            self.tenso_data["ch2_tso1"] = data[1]
            self.tenso_data["ch3_tso1"] = data[2]
        else:
            self.tenso_data["ch1_tso2"] = data[0]
            self.tenso_data["ch2_tso2"] = data[1]
            self.tenso_data["ch3_tso2"] = data[2]
        
        if id == 1:
            self._make_calculations()

    def _make_calculations(self) -> None:
        # TEMP: store samples, average every 50, print on first console line, clear
        self._tenso_samples.append(list(self.tenso_data.values()))
        if len(self._tenso_samples) >= 50:
            n = len(self._tenso_samples)
            averages = [sum(col) / n for col in zip(*self._tenso_samples)]
            print(f"\033[H\033[K{averages}", flush=True)
            self._tenso_samples.clear()

        ch1_tso1 = self.tenso_data["ch1_tso1"]
        ch2_tso1 = self.tenso_data["ch2_tso1"]
        ch3_tso1 = self.tenso_data["ch3_tso1"]
        ch1_tso2 = self.tenso_data["ch1_tso2"]
        ch2_tso2 = self.tenso_data["ch2_tso2"]
        ch3_tso2 = self.tenso_data["ch3_tso2"]

        x = ch2_tso1 + ch3_tso1
        y = ch1_tso1
        z = ch1_tso2 + ch2_tso2 + ch3_tso2
        mx = -ch2_tso2*0.215 + ch1_tso2*0.215 - ch1_tso1*1.167
        my = -1.167*ch1_tso1 - 1.167*ch2_tso1-0.215*ch3_tso2 + 0.215*ch1_tso2+0.215*ch2_tso2
        mz = ch2_tso1*0.215 + ch3_tso1*0.215

        self.SCALE_DATA.emit({"x": x, "y": y, "z": z, "mx": mx, "my": my, "mz": mz})

    def _emit_read_data(self, data) -> None:
        self.POS_DATA.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def set_pitch_yaw_roll(self, pitch: float, yaw: float, roll: float) -> None:
        self._write_plc_float(self.write_nb, 4, pitch)
        self._write_plc_float(self.write_nb, 8, yaw)
        self._write_plc_float(self.write_nb, 12, roll)
        self.start_driver()

    def set_yaw(self, yaw: float):
        self._write_element(2, yaw)

    def set_pitch(self, pitch: float):
        self._write_element(6, pitch)

    def set_roll(self, roll: float):
        self._write_element(10, roll)

    def disconnect(self) -> None:
        for scanner in self.tenso_scanners:
            scanner.disconnect()
            scanner.wait(3000)
        super().disconnect()