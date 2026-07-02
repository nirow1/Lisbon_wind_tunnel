import time
from struct import unpack
from threading import Thread
from PySide6.QtCore import Signal
from Device_controllers.plc_controller import PLCController
from Utils.helper_functions import list_to_ushort, byte_to_bits


class TunnelPLCController(PLCController):
    TUNNEL_DATA = Signal(dict)
    CONTROL_BYTE = Signal(dict)
    PLC_DATA = Signal(dict)
    STATUS_DATA = Signal(dict)
    PARAM_DATA_FAN = Signal(dict)
    PARAM_DATA_STATUS = Signal(dict)

    def __init__(self, ip_address="192.168.1.1"):
        super().__init__(ip_address, read_nb=2, write_nb=3, param_nb=4)
        self.control_byte = {"start": 0, "stop": 0, "ack": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0,
                             "pump": 0, "cooling": 0, "PID": 0, "control": 0, "12": 0, "13": 0, "14": 0, "15": 0}
        self.PLC_CONNECTED.connect(self._read_plc_data_and_emit)

    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        while self.connected:
            try:
                main_data_dict = self._read_main_data()

                self.STATUS_DATA.emit(main_data_dict[0])
                self.TUNNEL_DATA.emit(main_data_dict[1])
                self.PARAM_DATA_FAN.emit(main_data_dict[2])
                self.PARAM_DATA_STATUS.emit(main_data_dict[3])
            except Exception as e:
                main_data_dict = {}
                print(e)

            time.sleep(0.1)

    def _read_main_data(self) -> list | None:
        try:
            plc_data = self._read_plc_data(
                self.read_nb,
                2,
                106,
                '>H2ff8xf8x2f4x2B5f7B5xf4xf4xf4xf'
            )

            # Split into original blocks
            status_bits = byte_to_bits(plc_data[0])
            b1 = plc_data[1:7]
            fan_data = plc_data[7:14]
            error_status = plc_data[14:21]
            b2 = plc_data[21:25]

            engine_rotations, wind_velocity, temp_entry, temp_exit, diff_pressure, diff_pressure_raw = b1
            temp_entry_maxmin, temp_exit_maxmin, pressure_maxmin, velocity_maxmin = b2

            average_temp = (temp_entry + temp_exit) / 2
            avg_temp_maxmin = (temp_entry_maxmin + temp_exit_maxmin) / 2

            return [{"rdy": status_bits[0], "running": status_bits[1], "error": status_bits[3],
                "warning": status_bits[4], "safety": status_bits[5],"e-stop": status_bits[6], "doors": status_bits[7],
                "concetrc": status_bits[8], "surge_protection": status_bits[9], "driver_error": status_bits[10],
                "pump_feedback": status_bits[11], "fire_alarm": status_bits[12], "fan_standstill": status_bits[13]},

                {"engine_rotations": round(engine_rotations, 2),
                "wind_velocity": round(wind_velocity, 2),
                "wind_velocity_maxmin": round(velocity_maxmin, 2),
                "average_temp": round(average_temp, 1),
                "temp_entry": round(temp_entry, 1),
                "temp_exit": round(temp_exit, 1),
                "avg_temp_maxmin": round(avg_temp_maxmin, 2),
                "diff_pressure": round(diff_pressure, 2),
                "diff_pressure_raw": round(diff_pressure_raw, 2),
                "pressure_maxmin": round(pressure_maxmin, 2),},

                {"driver_status": fan_data[0],
                "error_code": fan_data[1],
                "output": round(fan_data[2], 2),
                "current": round(fan_data[3], 2),
                "moment": round(fan_data[4], 2),
                "engine_temp": round(fan_data[5], 2),
                "converter_temp": round(fan_data[6], 2),},

                {"est_converter": error_status[0], "est_service": error_status[1], "est_measure_space": error_status[2],
                "est_entry_doors": error_status[3], "est_hexapod": error_status[4],
                "est_doors_meas_space": error_status[5], "est_doors_meas_space_2": error_status[6]
            }]
        except Exception as e:
            print(e)
            self._stop_timers()
            return None

    def set_engine_frequency(self, request: float):
        self._write_plc_float(self.write_nb, 4, request)

    def set_wind_velocity(self, velocity: float):
        self._write_plc_float(self.write_nb,8, velocity)

    def set_ramp_down(self, value: int):
        self._write_plc_int(self.param_nb, 50, value)

    def set_ramp_up(self, value: int):
        self._write_plc_int(self.param_nb, 48, value)

    def set_run_dur(self, value: int):
        self._write_plc_int(self.param_nb, 52, value)

    def set_pid(self, kp: float, ti: float, td: float):
        self._write_plc_float(self.param_nb,2, kp)
        self._write_plc_float(self.param_nb,6, ti)
        self._write_plc_float(self.param_nb,10, td)

    def switch_pid(self, state: bool):
        self.control_byte["PID"] = state

    def switch_pump(self, state: bool):
        self._switch_bit("pump", state)

    def switch_cooling(self, state: bool):
        self._switch_bit("cooling", state)

    def switch_control(self, state: bool):
        self.control_byte["control"] = state

    def start_engine(self):
        self.control_byte["start"] = 1
        self.control_byte["stop"] = 0
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_int(self.write_nb, 2, data_short)

    def read_parameter_data(self) -> tuple | None:
        return self._read_plc_data(self.param_nb, 0, 114, '>h4fxB7f3h2B9fhf8h')

    def stop_engine(self):
        self.control_byte["stop"] = 1
        self.control_byte["start"] = 0
        self.set_engine_frequency(0.0)
        self.set_wind_velocity(0.0)
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_int(self.write_nb, 2, data_short)

    def _switch_bit(self, attribute: str, state: bool):
        self.control_byte[attribute] = state
        data_short = list_to_ushort(list(self.control_byte.values()), msb_first=False)
        self._write_plc_int(self.write_nb, 2, data_short)

    def _read_control_byte(self) -> dict:
        data = self._read_plc_data(self.read_nb, 2, 2, '>H')
        if data is None:
            return {}
        value = data[0]
        keys = list(self.control_byte.keys())
        return {key: (value >> i) & 1 for i, key in enumerate(keys)}
