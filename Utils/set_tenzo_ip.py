import socket
import logging


class FJtechIPSocket(socket.socket):
    def __init__(self, socket_name, ip=None):  # , *args, **kwargs
        # super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        super(FJtechIPSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self._socket_name = socket_name
        self._ip = ip
        self._port = 23

        self.settimeout(2)
        self._f = self.makefile()
        logging.getLogger('comm_logger').info('Socket ' + self._socket_name + ' created')

    @property
    def socket_name(self):
        return self._socket_name

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        # TODO: Doplnit kontrolu formatu
        self._ip = ip

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    def fj_connect(self):
        """
        :return: True - connected
                False - disconnected
        """
        assert self._ip

        try:
            self.connect((self.ip, self.port))
            logging.getLogger('main_logger').info('Socket ' + self._socket_name + ' connected')
            return True
        except socket.error:
            logging.getLogger('main_logger').warning('Socket ' + self._socket_name + ' connection error.')
            return False

    def fj_disconnect(self):
        try:
            self.shutdown(socket.SHUT_RDWR)
            self.close()
            logging.getLogger('main_logger').warning('Socket ' + self._socket_name + ' disconnected.')
            return True
        except Exception as e:
            print(e)

    def fj_write_data_safe(self, data):
        try:
            if self.sendall(data.encode('ascii')):
                logging.getLogger('comm_logger').warning('--WRITE--> FAILED TO WRITE %s' % data)
            logging.getLogger('comm_logger').info('--WRITE--> %s' % data)
        except Exception as e:
            print(e)

    def fj_read_line_from_socket(self):
        buffer = b''
        while True:
            data = self.recv(1)
            if not data:
                break
            buffer += data
            buffer.decode('utf-8')
            if buffer.endswith(b'\n'):
                break
        return buffer.decode('utf-8')


if __name__ == '__main__':
    socket = FJtechIPSocket("tenzoscan", "192.168.1.98")
    socket.fj_connect()

    socket.send(b'AT+RAM_RW=0,1\r\n')
    echo = socket.fj_read_line_from_socket()
    waiting = socket.fj_read_line_from_socket()
    print(echo)
    print(waiting)

    socket.send(b'\x01')
    empty = socket.fj_read_line_from_socket()
    error = socket.fj_read_line_from_socket()
    print(empty)
    print(error)

    ip_add = [192, 168, 1, 8]
    byte_ip = bytearray(ip_add)
    socket.send(b'AT+EEPROM_RW=0,4\r\n')
    echo = socket.fj_read_line_from_socket()
    waiting = socket.fj_read_line_from_socket()
    print(echo)
    print(waiting)

    socket.send(byte_ip)
    empty = socket.fj_read_line_from_socket()
    error = socket.fj_read_line_from_socket()
    print(empty)
    print(error)

    socket.fj_disconnect()