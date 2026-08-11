import time
from threading import Thread
from PySide6.QtCore import Signal
from Utils.helper_functions import list_to_short, byte_to_bits, control_dict_to_bytes
from Device_controllers.plc_controller import PLCController


class TunnelPLCController(PLCController):
    SENSOR_VALUES = Signal(dict)
    CONTROL_BYTE = Signal(dict)
    PLC_DATA = Signal(dict)
    STATUS_DATA = Signal(dict)
    DRIVER_DATA = Signal(dict)
    SAFETY_DIAGNOSTICS = Signal(dict)

    def __init__(self, ip_address="192.168.10.1"):
        super().__init__(ip_address, read_nb=101, write_nb=100, param_nb=102)
        self.control_byte = { "start": 0, "stop": 0, "ack": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                             "8": 0, "PID": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0 }
        self.control_byte_map = { "start": 0, "stop": 1, "ack": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                             "8": 8, "PID": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15 }
        self.PLC_CONNECTED.connect(self._start_reading_plc_data)

    def _start_reading_plc_data(self, connected: bool = True):
        if not connected:
            return
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

                self.STATUS_DATA.emit(main_data_dict[0])
                self.SENSOR_VALUES.emit(main_data_dict[1])
                self.DRIVER_DATA.emit(main_data_dict[2])
                self.SAFETY_DIAGNOSTICS.emit(main_data_dict[3])
            except Exception as e:
                print(e)

            time.sleep(0.1)

    def _read_main_data(self) -> list[dict] | None:
        try:
            plc_data = self._read_plc_data(
                self.read_nb,
                0,
                84,
                '>2H2f3f3f3f3fBB5f2B'
            )
            self.watchdog_count = plc_data[0]
            status_bits = byte_to_bits(((plc_data[1] & 0xFF) << 8) | (plc_data[1] >> 8), "little")  # 16 bits from 2 bytes

            r_frequency, r_speed = plc_data[2:4]

            temp_input = plc_data[4:7]
            temp_output = plc_data[7:10]
            out_pressure = plc_data[10:13]
            anemometer = plc_data[13:16]

            driver_status = plc_data[16]
            error_code = plc_data[17]
            drive_data = plc_data[18:23]  # 5 floats: power, current, torque, motor_temp, drive_temp

            safety_data = plc_data[23:25]  # 2 bytes: estop_main, estop_panel

            average_temp = (temp_input[0] + temp_output[0]) / 2

            return [

                # -----------------------------------------------------
                # STATUS BITS
                # -----------------------------------------------------
                {
                    "rdy": status_bits[0], "running": status_bits[1], "idle": status_bits[2], "error": status_bits[3],
                    "warning": status_bits[4], "safety": status_bits[5], "e-stop": status_bits[6],
                    "doors": status_bits[7], "nozzle_present": status_bits[8], "reducer": status_bits[9],
                    "driver_error": status_bits[10], "surge_protection": status_bits[11], "fire_alarm": status_bits[12],
                    "fan_standstill": status_bits[13]
                },

                # -----------------------------------------------------
                # SENSOR VALUES
                # -----------------------------------------------------
                {
                    "frequency": round(r_frequency, 2), "speed": round(r_speed, 2),

                    "temp_input_raw": round(temp_input[0], 2),
                    "temp_input_filtered": round(temp_input[1], 2),
                    "temp_input_smoothed": round(temp_input[2], 2),

                    "temp_output_raw": round(temp_output[0], 2),
                    "temp_output_filtered": round(temp_output[1], 2),
                    "temp_output_smoothed": round(temp_output[2], 2),

                    "pressure_raw": round(out_pressure[0], 2),
                    "pressure_filtered": round(out_pressure[1], 2),
                    "pressure_smoothed": round(out_pressure[2], 2),

                    "wind_raw": round(anemometer[0], 2),
                    "wind_filtered": round(anemometer[1], 2),
                    "wind_smoothed": round(anemometer[2], 2),

                    "average_temp": round(average_temp, 1)
                },

                # -----------------------------------------------------
                # DRIVE DATA
                # -----------------------------------------------------
                {
                    "driver_status": driver_status, "error_code": error_code, "power": round(drive_data[0], 2),
                    "current": round(drive_data[1], 2), "torque": round(drive_data[2], 2),
                    "motor_temp": round(drive_data[3], 2), "drive_temp": round(drive_data[4], 2)
                },

                # -----------------------------------------------------
                # SAFETY DIAGNOSTICS
                # -----------------------------------------------------
                {
                    "estop_main": safety_data[0], "estop_panel": safety_data[1]
                }
            ]

        except Exception as e:
            print(e)
            self._stop_timers()
            return None

    def set_engine_frequency(self, request: float):
        self._write_plc_float(self.write_nb, 4, request)

    def set_wind_velocity(self, velocity: float):
        self._write_plc_float(self.write_nb,8, velocity)

    def set_pid(self, kp: float, ti: float, td: float):
        self._write_plc_float(self.param_nb,2, kp)
        self._write_plc_float(self.param_nb,6, ti)
        self._write_plc_float(self.param_nb,10, td)

    def switch_pid(self, state: bool):
        # TRUE -> Frequency, FALSE -> PID regulation
        self.control_byte["PID"] = int(state)

    def start_engine(self):
        self.control_byte["start"] = 1
        self.control_byte["stop"] = 0
        data_short = control_dict_to_bytes(self.control_byte, self.control_byte_map, endian="little")
        self._write_plc_data(self.write_nb, 2, 2,  data_short)

    def read_parameter_data(self) -> tuple | None:
        return self._read_plc_data(self.param_nb, 0, 84, '>h9fH9f2Hf')

    def set_parameter_data(self, values: dict):
        if not self.connected:
            return

        # REAL (Float) parameters: {byte_offset: param_name}
        real_map = {
            30: "rQ",               34: "rR",
            40: "rLowSpeed",        44: "rLowKp",
            48: "rHighSpeed",       52: "rHighKp",
            56: "rGain",            60: "rTi",
            64: "rTd",              68: "rDeadband",
            72: "rPID_FilterTd",    80: "rFF_K_Step",
        }
        for pos in real_map:
            if pos in values:
                self._write_plc_float(self.param_nb, pos, float(values[pos]))

        # INT parameters
        if 0 in values:  # iNoiseThresholdPressure
            self._write_plc_int(self.param_nb, 0, int(values[0]))

        # BOOL parameters
        # Byte 38 → xUseGainScheduling (bit 0 only — write full byte)
        if 38.0 in values:
            self._write_plc_bool_byte(self.param_nb, 38, int(values[38.0]))

        # Byte 76 → xDonPV (bit 1), xPonPV (bit 2) — multiple bits, read-modify-write
        bool_76 = {76.1: 1, 76.2: 2}
        if any(k in values for k in bool_76):
            self._write_plc_bits(self.param_nb, 76, {bit: int(values[k]) for k, bit in bool_76.items() if k in values})

        # Byte 78 → xUseFeedForward (bit 0 only — write full byte)
        if 78.0 in values:
            self._write_plc_bool_byte(self.param_nb, 78, int(values[78.0]))

    def stop_engine(self):
        self.control_byte["stop"] = 1
        self.control_byte["start"] = 0
        self.set_engine_frequency(0.0)
        self.set_wind_velocity(0.0)
        data_short = list_to_short(list(self.control_byte.values()), msb_first=False)
        self._write_plc_int(self.write_nb, 2, data_short)

    def _switch_bit(self, attribute: str, state: bool):
        self.control_byte[attribute] = state
        data_short = list_to_short(list(self.control_byte.values()), msb_first=False)
        self._write_plc_int(self.write_nb, 2, data_short)

    def _read_control_byte(self) -> dict:
        data = self._read_plc_data(self.read_nb, 2, 2, '>H')
        if data is None:
            return {}
        value = data[0]
        keys = list(self.control_byte.keys())
        return {key: (value >> i) & 1 for i, key in enumerate(keys)}

if __name__ == '__main__':
    tunnel_plc = TunnelPLCController()
    tunnel_plc.start()
