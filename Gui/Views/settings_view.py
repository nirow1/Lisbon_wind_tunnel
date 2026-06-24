from threading import Thread
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from Device_controllers.plc_controller import PLCController
from Qt_files.Qt_python.ui_wind_tunnel_settings_view import Ui_Form


class SettingsView(QWidget):
    RETURN_TO_MAIN = Signal()

    def __init__(self, plc: PLCController):
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
        order = [0, 2, 6, 10, 80, 14, 54.2, 60, 64, 68, 72, 18.1, 18.2, 54.0, 24, 28, 54.1, 56, 94, 84, 88, 92]
        for row in range(len(order)):
            item = QTableWidgetItem("")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 0, item)

    def _bind_buttons(self):
        self.ui.set_changes_btn.clicked.connect(self._set_values)

    def _bind_emits(self):
        # PLC_CONNECTED emits bool — call _confirm_changes only on connect
        self.plc.PLC_CONNECTED.connect(lambda connected: self._confirm_changes() if connected else None)

    def _set_values(self):
        order = [0, 2, 6, 10, 80, 14, 54.2, 60, 64, 68, 72, 18.1, 18.2, 54.0, 24, 28, 54.1, 56, 94, 84, 88, 92]
        values = {}
        for row, key in enumerate(order):
            item = self.ui.tableWidget.item(row, 1)
            values[key] = float(item.text()) if item is not None else 0.0

        Thread(target=self._send_and_confirm, args=(values,), daemon=True).start()

    def _send_and_confirm(self, values: dict):
        self.plc.set_parameter_data(values)
        self._confirm_changes()

    def _confirm_changes(self):
        data = self.plc.read_parameter_data()
        if data is None:
            return

        bool_18 = data[5]
        bool_54 = data[16]

        data_dict = {
            0: data[0], 2: data[1], 6: data[2], 10: data[3], 14: data[4],
            18.1: (bool_18 >> 1) & 1, 18.2: (bool_18 >> 2) & 1,
            24: data[7], 28: data[8],
            54.0: (bool_54 >> 0) & 1, 54.1: (bool_54 >> 1) & 1, 54.2: (bool_54 >> 2) & 1,
            56: data[18], 60: data[19], 64: data[20], 68: data[21], 72: data[22],
            80: data[24], 84: data[25], 88: data[26], 92: data[27], 94: data[28],
        }

        order = [0, 2, 6, 10, 80, 14, 54.2, 60, 64, 68, 72, 18.1, 18.2, 54.0, 24, 28, 54.1, 56, 94, 84, 88, 92]
        for row, key in enumerate(order):
            non_editable_0 = QTableWidgetItem(str(data_dict.get(key, "")))
            non_editable_0.setFlags(non_editable_0.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 0, non_editable_0)

            non_editable_1 = QTableWidgetItem(str(data_dict.get(key, "")))
            self.ui.tableWidget.setItem(row, 1, non_editable_1)
