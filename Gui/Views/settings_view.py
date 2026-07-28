from threading import Thread
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from Qt_files.Qt_python.ui_wind_tunnel_settings_view import Ui_Form
from Device_controllers.tunnel_plc_controller import TunnelPLCController


class SettingsView(QWidget):
    RETURN_TO_MAIN = Signal()

    def __init__(self, plc: TunnelPLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._average_speed = [0]
        self._req_velocity: float = 0.0

        self.regulation: bool = False

        self.plc = plc
        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        order = [0, 30, 34, 38, 40, 44, 48, 52, 56, 60, 64, 68, 72,76.1, 76.2, 78, 80]
        for row in range(len(order)):
            item = QTableWidgetItem("")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 0, item)

    def _bind_buttons(self):
        self.ui.set_changes_btn.clicked.connect(self._set_values)

    def _bind_emits(self):
        # PLC_CONNECTED emits bool — call _confirm_changes only on connect
        self.plc.PLC_CONNECTED.connect(lambda connected: self._check_parameters() if connected else None)

    def _set_values(self):
        order = [0, 30, 34, 38, 40, 44, 48, 52, 56, 60, 64, 68, 72,76.1, 76.2, 78, 80]
        values = {}
        for row, key in enumerate(order):
            item = self.ui.tableWidget.item(row, 1)
            values[key] = float(item.text()) if item is not None else 0.0

        Thread(target=self._send_and_confirm, args=(values,), daemon=True).start()

    def _send_and_confirm(self, values: dict):
        self.plc.set_parameter_data(values)
        self._check_parameters()

    def _check_parameters(self):
        data = self.plc.read_parameter_data()
        if data is None:
            return

        bool_38 = data[10]
        bool_76 = data[20]
        bool_78 = data[21]

        data_dict = {
            0: data[0], 2: data[1], 6: data[2], 10: data[3], 14: data[4],
            18: data[5], 22: data[6], 26: data[7], 30: data[8], 34: data[9], 38: bool_38,
            40: data[11], 44: data[12], 48: data[13], 50: data[14], 56: data[15], 60: data[16],
            64: data[17], 68: data[18], 72: data[19],
            76.1: (bool_76 >> 1) & 1, 76.2: (bool_76 >> 2) & 1,
            78: bool_78, 80: data[22]
        }

        order = [0, 30, 34, 38, 40, 44, 48, 52, 56, 60, 64, 68, 72,76.1, 76.2, 78, 80]
        for row, key in enumerate(order):
            non_editable_0 = QTableWidgetItem(str(data_dict.get(key, "")))
            non_editable_0.setFlags(non_editable_0.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 0, non_editable_0)

            non_editable_1 = QTableWidgetItem(str(data_dict.get(key, "")))
            self.ui.tableWidget.setItem(row, 1, non_editable_1)
