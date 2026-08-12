from datetime import datetime, timezone
from threading import Thread
from time import sleep

from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator
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

        self.current_x_2d = 0.0
        self.current_y_2d = 0.0
        self.current_x_3d = 0.0
        self.current_y_3d = 0.0
        self.current_z_3d = 0.0

        self.field_2d = PositionFieldWidget(1000,
                                            1000,
                                            400,
                                            400)
        self.ui.field_2d_lo.addWidget(self.field_2d)

        self.field_3d_xy = PositionFieldWidget(1470,1470, 350, 350)
        self.ui.field_3d_xy_lo.addWidget(self.field_3d_xy)
        self.field_3d_xz = PositionFieldWidget(1470,850, 350, 350)
        self.ui.field_3d_xz_lo.addWidget(self.field_3d_xz)

        self.test_plan_2d = TestPlanTab(["Pos X","Pos Y"])
        self.ui.test_plan_2d_lo.addWidget(self.test_plan_2d)

        self.test_plan_3d = TestPlanTab(["Pos X","Pos Y","Pos Z"])
        self.ui.test_plan_3d_lo.addWidget(self.test_plan_3d)

        self._init_graphical_changes()
        self._bind_buttons()

        self.ui.set_pos_x_2d_le.setValidator(QIntValidator(0, 1000))
        self.ui.set_pos_y_2d_le.setValidator(QIntValidator(0, 1000))
        self.ui.set_pos_x_3d_le.setValidator(QIntValidator(0, 1050))
        self.ui.set_pos_y_3d_le.setValidator(QIntValidator(0, 1040))
        self.ui.set_pos_z_3d_le.setValidator(QIntValidator(0, 605))

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

        self.ui.stop_driver_3d_btn.clicked.connect(self.plc_3d.stop_driver)
        self.ui.stop_driver_2d_btn.clicked.connect(self.plc_2d.stop_driver)

        self.test_plan_3d.ui.start_test_plan_btn.clicked.connect(self._start_3d_test_plan)
        self.test_plan_3d.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def _bind_emits(self):
        self.plc_3d.DRIVERS_POS.connect(self._show_3d_drivers_pos)
        self.plc_3d.STATUS_DATA.connect(self.set_status_data)
        self.plc_3d.PLC_CONNECTED.connect(self._on_plc_3d_connected)
        self.plc_2d.DRIVERS_POS.connect(self._show_2d_drivers_pos)
        self.plc_2d.PLC_CONNECTED.connect(self._on_plc_2d_connected)
        self.TEST_RUNNING.connect(self._set_buttons_state)

    def _on_plc_3d_connected(self, connected: bool):
        self.ui.connected_message_wg_2.setVisible(not connected)

    def _on_plc_2d_connected(self, connected: bool):
        self.ui.connected_message_wg.setVisible(not connected)

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

    def _set_buttons_state(self, running: bool):
        enabled = not running
        self.ui.set_pos_x_2d_btn.setEnabled(enabled)
        self.ui.set_pos_y_2d_btn.setEnabled(enabled)
        self.ui.set_pos_x_3d_btn.setEnabled(enabled)
        self.ui.set_pos_y_3d_btn.setEnabled(enabled)
        self.ui.set_pos_z_3d_btn.setEnabled(enabled)

    def _show_2d_drivers_pos(self, pos: dict):
        self.current_x_2d = pos.get("x", 0)
        self.current_y_2d = pos.get("y", 0)
        self.field_2d.update_position(self.current_x_2d, self.current_y_2d)

    def _show_3d_drivers_pos(self, pos: dict):
        self.current_x_3d = pos.get("x", 0)
        self.current_y_3d = pos.get("y", 0)
        self.current_z_3d = pos.get("z", 0)

        self.field_3d_xy.update_position(self.current_x_3d, self.current_y_3d)
        self.field_3d_xz.update_position(self.current_x_3d, self.current_z_3d)

        self.ui.set_pos_x_3d_lbl.setText(str(round(self.current_x_3d, 2)))
        self.ui.set_pos_y_3d_lbl.setText(str(round(self.current_y_3d, 2)))
        self.ui.set_pos_z_3d_lbl.setText(str(round(self.current_z_3d, 2)))

    def set_x_pos_2d(self):
        x_pos = float(self.ui.set_pos_x_2d_le.text())
        self.set_all_positions_2d(x_pos, self.current_y_2d)

    def set_y_pos_2d(self):
        y_pos = float(self.ui.set_pos_y_2d_le.text())
        self.set_all_positions_2d(self.current_x_2d, y_pos)

    def set_x_pos_3d(self):
        x_pos = float(self.ui.set_pos_x_3d_le.text())
        self.set_all_positions_3d(x_pos, self.current_y_3d, self.current_z_3d)

    def set_y_pos_3d(self):
        y_pos = float(self.ui.set_pos_y_3d_le.text())
        self.set_all_positions_3d(self.current_x_3d, y_pos, self.current_z_3d)

    def set_z_pos_3d(self):
        z_pos = float(self.ui.set_pos_z_3d_le.text())
        self.set_all_positions_3d(self.current_x_3d, self.current_y_3d, z_pos)

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
                self.test_plan_2d,
            ),
            daemon=True,
        ).start()

    def _start_3d_test_plan(self):
        Thread(
            target=self._run_test_plan,
            args=(
                self.test_plan_3d.get_test_plan(),
                self.set_all_positions_3d,
                self.test_plan_3d,
            ),
            daemon=True,
        ).start()

    def _run_test_plan(self, test_plan: list, set_positions, plan_tab: TestPlanTab):
        self.TEST_RUNNING.emit(True)
        plan_tab.show_message(True)
        try:
            for row in test_plan:
                self._wait_until(add_sec_to_current_time(row[0]))

                if self.stop_plan:
                    self.stop_plan = False
                    break

                positions = [
                    float(pos) if pos != "" else 0
                    for pos in row[1:]
                ]

                set_positions(*positions)
                self._wait_until_correct_pos()
        except Exception as e:
            print(f"Test plan error: {e}")
        finally:
            plan_tab.show_message(False)
            self.TEST_RUNNING.emit(False)

    def _wait_until(self, target_time: datetime):
        while datetime.now(timezone.utc) < target_time and not self.stop_plan:
            sleep(0.1)

    def _wait_until_correct_pos(self):
        # PLC status lags the command; without this settle time the loop exits
        # immediately while still ready/not-moving and every point is fired at once.
        sleep(0.3)
        while (not self.ready or self.moving) and not self.stop_plan:
            sleep(0.1)

    def _stop_plan(self):
        self.stop_plan = True