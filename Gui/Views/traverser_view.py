from datetime import datetime
from threading import Thread
from time import sleep

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from Device_controllers.driver_2d_plc_controller import Driver2DPLCController
from Device_controllers.driver_3d_plc_controller import Driver3DPLCController
from Gui.Custom_functions.test_plan_tab import TestPlanTab
from Gui.Custom_widgets.pos_field_view import PositionFieldWidget
from Qt_files.Qt_python.ui_wind_tunnel_traverser_view import Ui_Form
from Utils.static_methods import add_sec_to_current_time


class TraverserView(QWidget):
    TEST_RUNNING = Signal(bool)

    def __init__(self, plc_3d: Driver3DPLCController, plc_2d: Driver2DPLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False
        self.plc_3d = plc_3d
        self.plc_2d = plc_2d

        self.ready = 1
        self.moving = 0

        self.field_2d = PositionFieldWidget(1000,
                                            1000,
                                            400,
                                            400)
        self.ui.field_2d_lo.addWidget(self.field_2d)

        self.field_3d_xy = PositionFieldWidget(1000,1000, 350, 350)
        self.ui.field_3d_xy_lo.addWidget(self.field_3d_xy)
        self.field_3d_xz = PositionFieldWidget(1000,1000, 350, 350)
        self.ui.field_3d_xz_lo.addWidget(self.field_3d_xz)

        self.test_plan_2d = TestPlanTab(["Pos X","Pos Y"])
        self.ui.test_plan_2d_lo.addWidget(self.test_plan_2d)

        self.test_plan_3d = TestPlanTab(["Pos X","Pos Y","Pos Z"])
        self.ui.test_plan_3d_lo.addWidget(self.test_plan_3d)

        self._init_graphical_changes()
        self._bind_buttons()

        #self.ui.set_pos_x_2d_le.setValidator(IntValidator(0))
        #self.ui.set_pos_y_2d_le.setValidator(FloatValidator(0, 483))

        self._bind_emits()

    def _init_graphical_changes(self):
        self.test_plan_2d.show_message(False)
        self.test_plan_3d.show_message(False)

    def _bind_buttons(self):
        self.ui.pg_2d_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.drivers_2d_pg))
        self.ui.pg_3d_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.drivers_3d_pg))

        self.ui.set_pos_x_2d_btn.clicked.connect(self.set_x_pos_2d)
        self.ui.set_pos_y_2d_btn.clicked.connect(self.set_y_pos_2d)

        self.ui.set_pos_x_3d_btn.clicked.connect(self.set_x_pos_3d)
        self.ui.set_pos_y_3d_btn.clicked.connect(self.set_y_pos_3d)
        self.ui.set_pos_z_3d_btn.clicked.connect(self.set_z_pos_3d)

        self.test_plan_2d.ui.start_test_plan_btn.clicked.connect(self._start_test_plan)
        self.test_plan_2d.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

        self.ui.continue_btn.clicked.connect(self._accept_alert_message)

        self.test_plan_3d.ui.start_test_plan_btn.clicked.connect(self._start_3d_test_plan)
        self.test_plan_3d.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def _bind_emits(self):
        self.plc_3d.DRIVERS_POS.connect(self._show_3d_drivers_pos)
        self.plc_3d.STATUS_DATA.connect(self.set_status_data)
        self.plc_3d.PLC_CONNECTED.connect(lambda state: self.ui.connected_message_wg_2.setVisible(state))
        self.plc_2d.PLC_CONNECTED.connect(lambda state: self.ui.connected_message_wg.setVisible(state))
        self.TEST_RUNNING.connect(self._set_buttons_state)

    def set_status_data(self, status_data: dict):
        self.ready = status_data.get("ready", 0)
        self.moving = status_data.get("moving", 0)

    def show_alert_message(self,):
        self.ui.pg_2d_btn.hide()
        self.ui.pg_3d_btn.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def _accept_alert_message(self):
        self.ui.pg_2d_btn.show()
        self.ui.pg_3d_btn.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.drivers_2d_pg)

    def _set_buttons_state(self, state: bool):
        self.ui.set_pos_x_2d_btn.setEnabled(state)
        self.ui.set_pos_y_2d_btn.setEnabled(state)
        self.ui.set_pos_x_3d_btn.setEnabled(state)
        self.ui.set_pos_y_3d_btn.setEnabled(state)
        self.ui.set_pos_z_3d_btn.setEnabled(state)
        
    def _show_3d_drivers_pos(self, pos: dict):
        x_3d = pos.get("x", 0)
        y_3d = pos.get("y", 0)
        z_3d = pos.get("z", 0)

        # Update the positions based on the dictionary received from the PLC
        self.field_3d_xy.update_position(x_3d, y_3d)
        self.field_3d_xz.update_position(x_3d, z_3d)

        self.ui.set_pos_x_3d_lbl.setText(str(round(x_3d, 2)))
        self.ui.set_pos_y_3d_lbl.setText(str(round(y_3d, 2)))
        self.ui.set_pos_z_3d_lbl.setText(str(round(z_3d, 2)))

    def set_x_pos_2d(self):
        pos = float(self.ui.set_pos_x_2d_le.text())
        self.plc_2d.set_2d_x(pos)
        self.plc_2d.start_driver()

    def set_y_pos_2d(self):
        pos = float(self.ui.set_pos_y_2d_le.text())
        self.plc_2d.set_2d_y(pos)
        self.plc_2d.start_driver()

    def set_x_pos_3d(self):
        pos = float(self.ui.set_pos_x_3d_le.text())
        self.plc_3d.set_3d_x(pos)
        self.plc_3d.start_driver()

    def set_y_pos_3d(self):
        pos = float(self.ui.set_pos_y_3d_le.text())
        self.plc_3d.set_3d_y(pos)
        self.plc_3d.start_driver()

    def set_z_pos_3d(self):
        pos = float(self.ui.set_pos_z_3d_le.text())
        self.plc_3d.set_3d_z(pos)
        self.plc_3d.start_driver()

    def set_all_positions_2d(self, x_pos: float, y_pos: float):
        self.plc_2d.set_2d_pos(x_pos, y_pos)

    def set_all_positions_3d(self, x_pos: float, y_pos: float, z_pos: float):
        self.plc_3d.set_3d_pos(x_pos, y_pos, z_pos)

    def test_ver_pos(self, ver_pos):
        self.ui.set_pos_x_2d_le.setText(str(ver_pos))

    def test_hor_pos(self, hor_pos):
        self.ui.set_pos_y_2d_le.setText(str(hor_pos))

    def _start_test_plan(self):
        Thread(
            target=self._run_test_plan,
            args=(
                self.test_plan_2d.get_test_plan(),
                self.set_all_positions_2d,
            ),
        ).start()

    def _start_3d_test_plan(self):
        Thread(
            target=self._run_test_plan,
            args=(
                self.test_plan_3d.get_test_plan(),
                self.set_all_positions_3d,
            ),
        ).start()

    def _run_test_plan(self, test_plan: list, set_positions):
        self.TEST_RUNNING.emit(True)
        for row in test_plan:
            self._wait_until(add_sec_to_current_time(row[0]))

            if self.stop_plan:
                self.stop_plan = False
                break

            positions = [
                int(pos) if pos != "" else 0
                for pos in row[1:]
            ]

            set_positions(*positions)
            self._wait_until_correct_pos()
        self.TEST_RUNNING.emit(False)

    def _wait_until(self, target_time: datetime):
        while datetime.now() < target_time and not self.stop_plan:
            sleep(0.1)

    def _wait_until_correct_pos(self):
        while not self.ready and self.moving:
            sleep(0.1)

    def _stop_plan(self):
        self.stop_plan = True