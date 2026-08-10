import time
from time import sleep

from pymodbus.client import ModbusTcpClient as ModbusClient
from PySide6.QtCore import QThread, Signal

from Utils.static_methods import combine_to_float


class PapagoController(QThread):
    PAPAGO_DATA = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.10.13"
        self.port = 502
        self.client: ModbusClient | None = None
        self.connected: bool= False

    def run(self):
        self._connect_to_papago()

    def _connect_to_papago(self):
        while not self.connected:
            try:
                self.client = ModbusClient(self.ip, port=self.port)
                self.connected = self.client.connect()
                if self.connected:
                    self._read_papago_data()
                else:
                    sleep(5)
            except Exception as e:
                print(e)
                print("papago reading data error")

    def _read_papago_data(self):
        while self.connected:
            temp = self.client.read_input_registers(12, count=2)
            hum = self.client.read_input_registers(22, count=2)
            atmo_press = self.client.read_input_registers(32, count=2)
            if not temp.isError() and not hum.isError() and not atmo_press.isError():
                temp_float = round(combine_to_float(temp.registers), 1)
                hum_float = round(combine_to_float(hum.registers), 1)
                press_float = round(combine_to_float(atmo_press.registers), 1)
                papago_data = {"temperature": temp_float, "humidity": hum_float, "pressure": press_float}
                self.PAPAGO_DATA.emit(papago_data)
            time.sleep(0.3)

if __name__ == '__main__':
    papago = PapagoController()
    papago.run()