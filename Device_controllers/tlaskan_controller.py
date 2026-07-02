import threading
import logging
import socket
import time

from PySide6.QtCore import Signal, QThread
from struct import unpack


class TlaskanController(QThread):
    PRESSURE_DATA = Signal(list)

    def __init__(self, ip="192.168.1.8"):
        super().__init__()
        self.connected = False
        self.ip = ip
        self.port = 23
        self.msg = ""
        self.zero_values = [0.0 for _ in range(16)]
        self.processed_pressure = []

    def run(self):
        self._connect_to_tlaskan()

    def _connect_to_tlaskan(self):
        while not self.connected:
            try:
                self.tlaskan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tlaskan.connect((self.ip, self.port))
                self.connected = True
                self.tlaskan.send(b'AT+RAM_RW=5,1\x0d\x0a')
                self.tlaskan.send(b'\x01')
                self._start_communication()
                break
            except Exception as e:
                logging.getLogger().warning(F"failed to connect to TLASKAN: {e}")
                time.sleep(2)

    def _start_communication(self):
        request_thread = threading.Thread(target=self._send_measure_request)
        request_thread.start()
        self._listen_to_tls()

    def _send_measure_request(self):
        while self.connected:
            time.sleep(0.1)
            self.tlaskan.send(b'AT+RAM_RW=6,72,BIN,?\x0d\x0a')

    def _listen_to_tls(self):
        while self.connected:
            msg = self.tlaskan.recv(1024)
            self.msg = msg[22:94] #  +msg_2[22:46]
            print(self.msg)
            if len(self.msg) == 96:
                tlaskan_data = unpack("=BfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfBBfB", self.msg)
                self.msg = tlaskan_data[1::3]
                processed_pressure = [round(float(value), 3) for value in self.msg]
                self.processed_pressure = [i * 249.174 for i in processed_pressure]
                self.processed_pressure = [self.processed_pressure[i] - self.zero_values[i]
                                            for i in range(len(self.processed_pressure))]
                self.PRESSURE_DATA.emit(self.processed_pressure)

    def disconnect(self):
        self.connected = False
        time.sleep(0.2)
        self.tlaskan.close()

    def set_zero_values(self):
        if self.connected:
            print(self.processed_pressure)
            self.zero_values = [self.zero_values[i]+self.processed_pressure[i] for i in range(len(self.zero_values))]



if __name__ == '__main__':
    tls = TlaskanController()
    tls.run()
