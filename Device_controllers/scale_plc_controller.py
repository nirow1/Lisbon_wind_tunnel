import csv
from pathlib import Path
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

    COEFFS_PATH = Path("./App_data/scale_plc_coefficients.csv")

    def __init__(self, ip_address="192.168.10.12"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=4)
        self.tenso_scanners = (TensoScannerController("192.168.10.96"),
                               TensoScannerController("192.168.10.97"))
        self.tenso_data = {"ch1_tso1": 0, "ch2_tso1": 0, "ch3_tso1": 0,
                           "ch1_tso2": 0, "ch2_tso2": 0, "ch3_tso2": 0,}

        self._is_all_homed: bool | None = None
        # TEMP: collect samples for column averages
        self._tenso_samples: list[list] = []
        self._tare_offsets = [0.0] * 6
        self._last_raw_values = [0.0] * 6
        self._coeffs: list[list[float]] = []
        self._offsets: list[float] = []
        self.load_coefficients()
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
            self._make_calculations()

    def get_coefficients(self) -> tuple[list[list[float]], list[float]]:
        return [row[:] for row in self._coeffs], self._offsets[:]

    def set_coefficients(self, coeffs: list[list[float]], offsets: list[float]) -> None:
        self._coeffs = [row[:] for row in coeffs]
        self._offsets = offsets[:]
        self.save_coefficients()

    def reset_coefficients(self) -> None:
        self.load_coefficients()

    def load_coefficients(self) -> None:
        if not self.COEFFS_PATH.exists():
            self._coeffs = [[0.0] * 6 for _ in range(6)]
            self._offsets = [0.0] * 6
            self.save_coefficients()
            return
        with self.COEFFS_PATH.open(newline="") as f:
            rows = list(csv.reader(f))
        # Excel-like: header + S1..S6 + Offset row, columns Fx..Mz
        body = rows[1:] if rows and rows[0] and rows[0][0] == "" else rows
        self._coeffs = [[float(v) for v in row[1:7]] for row in body[:6]]
        self._offsets = [float(v) for v in body[6][1:7]]

    def save_coefficients(self) -> None:
        self.COEFFS_PATH.parent.mkdir(parents=True, exist_ok=True)
        with self.COEFFS_PATH.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["", "Fx", "Fy", "Fz", "Mx", "My", "Mz"])
            for i, row in enumerate(self._coeffs):
                writer.writerow([f"S{i + 1}", *row])
            writer.writerow(["Offset", *self._offsets])

    def tare(self) -> None:
        self._tare_offsets = self._last_raw_values[:]

    def _make_calculations(self) -> None:
        sensors = [
            self.tenso_data["ch1_tso1"],
            self.tenso_data["ch2_tso1"],
            self.tenso_data["ch3_tso1"],
            self.tenso_data["ch1_tso2"],
            self.tenso_data["ch2_tso2"],
            self.tenso_data["ch3_tso2"],
        ]
        coeffs, offsets = self._coeffs, self._offsets
        raw = [
            sum(sensors[i] * coeffs[i][j] for i in range(6)) + offsets[j]
            for j in range(6)
        ]
        self._last_raw_values = raw
        values = [raw[j] - self._tare_offsets[j] for j in range(6)]
        self.SCALE_DATA.emit({"x": values[0], "y": values[1], "z": values[2],
                              "mx": values[3], "my": values[4], "mz": values[5]})

    def _emit_read_data(self, data) -> None:
        self.POS_DATA.emit(data[0])
        self.STATUS_DATA.emit(data[1])

    def home_scale(self):
        super().home_driver(18)

    def set_pitch_yaw_roll(self, pitch: float, yaw: float, roll: float) -> None:
        self.set_pitch(pitch)
        self.set_yaw(yaw)
        self.set_roll(roll)
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