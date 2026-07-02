import time
from threading import Thread
from PySide6.QtCore import Signal
from Device_controllers.plc_controller import PLCController


class ScalePLCController(PLCController):
    SCALE_DATA = Signal(dict)

    def __init__(self, ip_address="192.168.1.1"):
        super().__init__(ip_address, read_nb=2, write_nb=3, param_nb=4)
        self.PLC_CONNECTED.connect(self._start_reading_plc_data)

    def _start_reading_plc_data(self):
        read_thread = Thread(target=self._read_plc_data_and_emit, daemon=True)
        read_thread.start()

    def _read_plc_data_and_emit(self):
        while self.connected:
            try:
                main_data_dict = self._read_main_data()
            except Exception as e:
                main_data_dict = {}
                print(e)

            time.sleep(0.1)

    def _read_main_data(self) -> dict | None:
        try:
            b1 = self._read_plc_data(self.read_nb, 4, 40, '>40B')

            return {key: value for key, value in enumerate(b1)}

        except Exception as e:
            print(e)
            self._stop_timers()
            return None
