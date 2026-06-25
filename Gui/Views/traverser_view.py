from datetime import datetime
from threading import Thread
from time import sleep

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Qt_files.Qt_python.ui_wind_tunnel_traverser_view import Ui_Form
from Utils.number_validator import IntValidator, FloatValidator


class TraverserView(QWidget):
    TEST_RUNNING = Signal(bool)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False

        self._init_graphical_changes()
        #self._bind_function_buttons()

        self.ui.set_pos_x_2d_le.setValidator(IntValidator(0))
        self.ui.set_pos_y_2d_le.setValidator(FloatValidator(0, 483))

        #self.bind_emits()

    def _init_graphical_changes(self):
        self.ui.test_running_wg.setVisible(False)
        self.ui.tableWidget.verticalHeader().setVisible(False)

    def _bind_function_buttons(self):

        self.ui.set_pos_x_2d_btn.clicked.connect(
            lambda: self.drivers.set_position(int(self.ui.set_pos_x_2d_le.text()), 1))
        self.ui.set_pos_y_2d_btn.clicked.connect(
            lambda: self.drivers.set_position(int(self.ui.set_pos_y_2d_le.text()), 2))

        # tab
        self.ui.add_row_btn.clicked.connect(self._add_row)
        self.ui.delete_row_btn.clicked.connect(self._delete_row)

        self.ui.start_test_plan_btn.clicked.connect(self._start_test_plan)
        self.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def bind_emits(self):
        self.drivers.VERTICAL_POS.connect(self.test_ver_pos)
        self.drivers.HORIZONTAL_POS.connect(self.test_hor_pos)
        self.TEST_RUNNING.connect(self._show_test_state)

    def test_ver_pos(self, ver_pos):
        self.ui.set_pos_x_2d_le.setText(str(ver_pos))

    def test_hor_pos(self, hor_pos):
        self.ui.set_pos_y_2d_le.setText(str(hor_pos))

    def _start_test_plan(self):
        Thread(target=self._test_plan_tread).start()

    def _test_plan_tread(self):
        test_plan = self._create_test_plan()
        self.TEST_RUNNING.emit(True)
        for row in test_plan:
            self._wait_until(row[0])

            if self.stop_plan:
                self.stop_plan = False
                break
            self.drivers.set_position(int(row[1]), 1) if row[1] != "" else None
            self.drivers.set_position(int(row[2]), 2) if row[2] != "" else None
        self.TEST_RUNNING.emit(False)

    def _wait_until(self, target_time: datetime):
        while datetime.now() < target_time and not self.stop_plan:
            sleep(0.1)

    def _add_row(self):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

    def _delete_row(self):
        row_position = self.ui.tableWidget.rowCount()
        if row_position > 0:
            self.ui.tableWidget.removeRow(row_position - 1)

    def _create_test_plan(self) -> list:
        table = self.ui.tableWidget
        rows = table.rowCount()
        cols = table.columnCount()
        data: list[list[str]] = []

        for r in range(rows):
            row_values: list[str] = []
            for c in range(cols):
                item = table.item(r, c)
                row_values.append(item.text() if item is not None else "")
            data.append(row_values)

        test_plan = []
        for row in data:
            test_plan.append((create_datetime(row[:3]),
                              float(row[3]) if row[3] != "" else "",
                              float(row[4]) if row[4] != "" else ""))

        return test_plan

    def _show_test_state(self, state: bool):
        self.ui.test_running_wg.setVisible(state)

    def _stop_plan(self):
        self.stop_plan = True