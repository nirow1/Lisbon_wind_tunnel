from datetime import datetime
from threading import Thread
from time import sleep
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Device_controllers.driver_plc_controlle import DriverPLCController
from Gui.Custom_widgets.pos_field_view import PositionFieldWidget
from Qt_files.Qt_python.ui_wind_tunnel_traverser_view import Ui_Form
from Utils.number_validator import IntValidator, FloatValidator


class TraverserView(QWidget):
    TEST_RUNNING = Signal(bool)

    def __init__(self, plc: DriverPLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False
        self.plc = plc

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
        self.ui.add_row_btn.clicked.connect(self._add_row)
        self.ui.delete_row_btn.clicked.connect(self._delete_row)

        self.ui.start_test_plan_btn.clicked.connect(self._start_test_plan)
        self.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def bind_emits(self):
        self.plc.DRIVERS_POS.connect(self.show_drivers_pos)

    def show_drivers_pos(self, pos: dict):
        x_2d = pos.get("x_2d", 0)
        y_2d = pos.get("y_2d", 0)
        x_3d = pos.get("x_3d", 0)
        y_3d = pos.get("y_3d", 0)
        z_3d = pos.get("z_3d", 0)

        # Update the positions based on the dictionary received from the PLC
        self.field_2d.update_position(x_2d, y_2d)
        self.field_3d_xy.update_position(x_3d, y_3d)
        self.field_3d_xz.update_position(x_3d, z_3d)

        self.ui.pos_x_2d_lbl.setText(str(round(x_2d, 2)))
        self.ui.pos_y_2d_lbl.setText(str(round(y_2d, 2)))
        self.ui.set_pos_x_3d_lbl.setText(str(round(x_3d, 2)))
        self.ui.set_pos_y_3d_lbl.setText(str(round(y_3d, 2)))
        self.ui.set_pos_z_3d_lbl.setText(str(round(z_3d, 2)))

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
        Thread(target=self._test_plan_tread).start()

    def _test_plan_tread(self):
        test_plan = self._create_test_plan()
        self.TEST_RUNNING.emit(True)
        for row in test_plan:
            self._wait_until(row[0])

            if self.stop_plan:
                self.stop_plan = False
                break
            self.set_x_pos_2d(int(row[1])) if row[1] != "" else None
            self.set_y_pos_2d(int(row[2])) if row[2] != "" else None
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