from datetime import datetime
from threading import Thread
from time import sleep
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Device_controllers.driver_plc_controlle import DriverPLCController
from Gui.Custom_widgets.pos_field_view import PositionFieldWidget
from Qt_files.Qt_python.ui_wind_tunnel_traverser_view import Ui_Form
from Utils.number_validator import IntValidator, FloatValidator
from Utils.static_methods import add_sec_to_current_time


class TraverserView(QWidget):
    TEST_RUNNING = Signal(bool)

    def __init__(self, plc: DriverPLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False
        self.plc = plc

        self.x_2d = 0
        self.y_2d = 0
        self.x_3d = 0
        self.y_3d = 0
        self.z_3d = 0

        self.field_2d = PositionFieldWidget(1000,
                                            1000,
                                            400,
                                            400)
        self.ui.field_2d_lo.addWidget(self.field_2d)

        self.field_3d_xy = PositionFieldWidget(1000,1000, 350,350)
        self.ui.field_3d_xy_lo.addWidget(self.field_3d_xy)
        self.field_3d_xz = PositionFieldWidget(1000,1000, 350, 350)
        self.ui.field_3d_xz_lo.addWidget(self.field_3d_xz)

        self._init_graphical_changes()
        self._bind_buttons()

        #self.ui.set_pos_x_2d_le.setValidator(IntValidator(0))
        #self.ui.set_pos_y_2d_le.setValidator(FloatValidator(0, 483))

        self.bind_emits()

    def _init_graphical_changes(self):
        self.ui.test_running_wg.setVisible(False)
        self.ui.tableWidget.verticalHeader().setVisible(False)

    def _bind_buttons(self):
        self.ui.pg_2d_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.drivers_2d_pg))
        self.ui.pg_3d_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.drivers_3d_pg))

        self.ui.set_pos_x_2d_btn.clicked.connect(self.set_x_pos_2d)
        self.ui.set_pos_y_2d_btn.clicked.connect(self.set_y_pos_2d)

        # tab
        self.ui.add_row_btn.clicked.connect(lambda: self._add_row(self.ui.tableWidget))
        self.ui.delete_row_btn.clicked.connect(lambda: self._delete_row(self.ui.tableWidget))

        self.ui.start_test_plan_btn.clicked.connect(self._start_test_plan)
        self.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

        #3d tab
        self.ui.add_3d_row_btn.clicked.connect(lambda: self._add_row(self.ui.tableWidget_3d))
        self.ui.delete_3d_row_btn.clicked.connect(lambda: self._delete_row(self.ui.tableWidget_3d))
        self.ui.start_3d_test_plan_btn.clicked.connect(self._start_3d_test_plan)
        self.ui.stop_3d_test_plan_btn.clicked.connect(self._stop_plan)

    def bind_emits(self):
        self.plc.DRIVERS_POS.connect(self.show_drivers_pos)

    def show_drivers_pos(self, pos: dict):
        self.x_2d = pos.get("x_2d", 0)
        self.y_2d = pos.get("y_2d", 0)
        self.x_3d = pos.get("x_3d", 0)
        self.y_3d = pos.get("y_3d", 0)
        self.z_3d = pos.get("z_3d", 0)

        # Update the positions based on the dictionary received from the PLC
        self.field_2d.update_position(self.x_2d, self.y_2d)
        self.field_3d_xy.update_position(self.x_3d, self.y_3d)
        self.field_3d_xz.update_position(self.x_3d, self.z_3d)

        self.ui.pos_x_2d_lbl.setText(str(round(self.x_2d, 2)))
        self.ui.pos_y_2d_lbl.setText(str(round(self.y_2d, 2)))
        self.ui.set_pos_x_3d_lbl.setText(str(round(self.x_3d, 2)))
        self.ui.set_pos_y_3d_lbl.setText(str(round(self.y_3d, 2)))
        self.ui.set_pos_z_3d_lbl.setText(str(round(self.z_3d, 2)))

    def set_y_pos_2d(self, pos: float):
        pass

    def set_x_pos_2d(self, pos: float):
        pass

    def set_x_pos_3d(self, pos: float):
        pass

    def set_y_pos_3d(self, pos: float):
        pass

    def set_z_pos_3d(self, pos: float):
        pass

    def test_ver_pos(self, ver_pos):
        self.ui.set_pos_x_2d_le.setText(str(ver_pos))

    def test_hor_pos(self, hor_pos):
        self.ui.set_pos_y_2d_le.setText(str(hor_pos))

    def _start_test_plan(self):
        Thread(
            target=self._run_test_plan,
            args=(
                self.ui.tableWidget,
                [self.set_x_pos_2d, self.set_y_pos_2d],
                lambda: (self.x_2d, self.y_2d),
            ),
        ).start()

    def _start_3d_test_plan(self):
        Thread(
            target=self._run_test_plan,
            args=(
                self.ui.tableWidget_3d,
                [self.set_x_pos_3d, self.set_y_pos_3d, self.set_z_pos_3d],
                lambda: (self.x_3d, self.y_3d, self.z_3d),
            ),
        ).start()

    def _run_test_plan(self, table, setters, get_current):
        test_plan = self._create_test_plan(table)
        self.TEST_RUNNING.emit(True)
        for row in test_plan:
            self._wait_until(add_sec_to_current_time(row[0]))

            if self.stop_plan:
                self.stop_plan = False
                break

            positions = row[1:]
            for setter, pos in zip(setters, positions):
                if pos != "":
                    setter(int(pos))

            self._wait_until_correct_pos(get_current, [int(pos) for pos in positions])
        self.TEST_RUNNING.emit(False)

    def _wait_until(self, target_time: datetime):
        while datetime.now() < target_time and not self.stop_plan:
            sleep(0.1)

    def _wait_until_correct_pos(self, get_current, targets):
        while not self.stop_plan:
            if all(abs(current - target) < 1 for current, target in zip(get_current(), targets)):
                break
            sleep(0.3)

    def _add_row(self, table):
        table.insertRow(table.rowCount())

    def _delete_row(self, table):
        row_count = table.rowCount()
        if row_count > 0:
            table.removeRow(row_count - 1)

    def _create_test_plan(self, table) -> list:
        test_plan = []
        for r in range(table.rowCount()):
            row_values = [
                table.item(r, c).text() if table.item(r, c) is not None else ""
                for c in range(table.columnCount())
            ]

            minutes = int(row_values[0]) if row_values[0] != "" else 0
            seconds = int(row_values[1]) if row_values[1] != "" else 0
            total_seconds = minutes * 60 + seconds

            positions = tuple(float(v) if v != "" else "" for v in row_values[2:])
            test_plan.append((total_seconds, *positions))

        return test_plan

    def _show_test_state(self, state: bool):
        self.ui.test_running_wg.setVisible(state)

    def _stop_plan(self):
        self.stop_plan = True