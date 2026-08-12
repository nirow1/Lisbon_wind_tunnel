from threading import Thread
from time import sleep

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

        self._is_all_homed: bool | None = None
        # TEMP: collect samples for column averages
        self._tenso_samples: list[list] = []
        self.bind_emits()

    def _read_main_data(self) -> list | None:
        try:
            scale_data = self._read_plc_data(self.read_nb, 0, 34, '>4dH')

            status_data = byte_to_bits(((scale_data[4] & 0xFF) << 8) | (scale_data[4] >> 8), "little")

            self._is_all_homed = bool(status_data[10])

            return [{"roll": scale_data[2], "pitch": scale_data[1], "yaw": scale_data[0], "axis_4": scale_data[3]},
                    {"ready": status_data[0], "moving": status_data[2], "allhoomed": status_data[10]}]

        except Exception as e:
            print(e)
            return None

    def bind_emits(self) -> None:
        self.tenso_scanners[0].TENSO_DATA.connect(lambda data: self._handle_tenso_data(data, 1))
        self.tenso_scanners[1].TENSO_DATA.connect(lambda data: self._handle_tenso_data(data, 2))
        self.PLC_CONNECTED.connect(self._on_plc_connected)

    def _on_plc_connected(self, connected: bool = True) -> None:
        if not connected:
            self._is_all_homed = None
            return
        self._is_all_homed = None
        self.connect_to_tenso_scanners()
        Thread(target=self._home_after_status, daemon=True).start()

    def _home_after_status(self) -> None:
        while self.connected and self._is_all_homed is None:
            sleep(0.05)
        if self.connected and not self._is_all_homed:
            self.home_scale()

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
        ch1_tso1 = self.tenso_data["ch1_tso1"]
        ch2_tso1 = self.tenso_data["ch2_tso1"]
        ch3_tso1 = self.tenso_data["ch3_tso1"]
        ch1_tso2 = self.tenso_data["ch1_tso2"]
        ch2_tso2 = self.tenso_data["ch2_tso2"]
        ch3_tso2 = self.tenso_data["ch3_tso2"]

        x = ch1_tso1 * -0.0000040934 + ch2_tso1 * 0.0000103008 + ch3_tso1 * -0.0000077890 + ch1_tso2 * 0.0000235612 + ch2_tso2 * 0.0001517056 + ch3_tso2 * 0.0001514674 - 2861.3773566694
        y = ch1_tso1 * 0.0000244077 + ch2_tso1 * -0.0000069629 + ch3_tso1 * -0.0000051808 + ch1_tso2 * 0.0001158091 + ch2_tso2 * -0.0000116837 + ch3_tso2 * -0.0000054757 - 1011.2072954020
        z = ch1_tso1 * 0.0001735134 + ch2_tso1 * 0.0005021131 + ch3_tso1 * 0.0004471496 + ch1_tso2 * 0.0002450960 + ch2_tso2 * -0.0000567972 + ch3_tso2 * -0.0001257411 - 9700.7692685649
        mx = ch1_tso1 * -0.0000106209 + ch2_tso1 * -0.0000196786 + ch3_tso1 * 0.0000265507 + ch1_tso2 * -0.0000072199 + ch2_tso2 * -0.0000312812 + ch3_tso2 * -0.0000281642 + 623.5219933303
        my = ch1_tso1 * -0.0000174044 + ch2_tso1 * 0.0000707668 + ch3_tso1 * -0.000032043 + ch1_tso2 * 0.0000658358 + ch2_tso2 * 0.0000262472 + ch3_tso2 * 0.0000221171 - 1436.6778343669
        mz = ch1_tso1 * -0.0000015874 + ch2_tso1 * -0.0000071138 + ch3_tso1 * 0.000033506 + ch1_tso2 * -0.000046326 + ch2_tso2 * -0.0000360606 + ch3_tso2 * 0.0000244908 + 193.3865058669

        self.SCALE_DATA.emit({"x": x, "y": y, "z": z, "mx": mx, "my": my, "mz": mz})

    def _emit_read_data(self, data) -> None:
        self.POS_DATA.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def home_scale(self):
        super().home_driver(18)

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