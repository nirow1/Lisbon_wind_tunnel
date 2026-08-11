from datetime import datetime
from threading import Thread
from time import sleep

from PySide6.QtWidgets import QWidget

from Device_controllers.scale_plc_controller import ScalePLCController
from Gui.Charts.zoomable_chart import ZoomableChart
from Gui.Custom_functions.test_plan_tab import TestPlanTab
from Qt_files.Qt_python.ui_wind_tunnel_scale_view import Ui_Form
from Utils.static_methods import add_sec_to_current_time


class ScaleView(QWidget):
    def __init__(self, scale_controller: ScalePLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False

        self.scale_chart = ZoomableChart("Balances",
                                              x_axis_seconds=600,
                                              y_axis=(-500, 500),
                                              line_name=["Fx","Fy","fz","Mx","My","Mz"],
                                              line_count=6)
        self.ui.scale_chart.addWidget(self.scale_chart)

        self.scales = scale_controller

        self.test_plan_wg = TestPlanTab(["Pitch", "Roll", "Yaw"])
        self.ui.test_plan_lo.addWidget(self.test_plan_wg)

        self._bind_buttons()
        self._bind_emits()
        self._initial_graphical_changes()

    def _initial_graphical_changes(self):
        self.ui.stackedWidget.setCurrentWidget(self.scale_chart)
        self.test_plan_wg.show_message(False)

    def _bind_buttons(self):
        self.ui.test_plan_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.test_plan_pg))
        self.ui.chart_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))

        self.test_plan_wg.ui.start_test_plan_btn.clicked.connect(self.start_test_plan)
        self.test_plan_wg.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def _bind_emits(self):
        self.scales.POS_DATA.connect(self._handle_pos_data)
        self.scales.SCALE_DATA.connect(self._handle_scale_data)
        self.scales.STATUS_DATA.connect(self._handle_status_data)
        self.scales.PLC_CONNECTED.connect(lambda state: self.ui.connected_message_wg.setVisible(state))
        
    def _handle_pos_data(self, data: dict):
        ...

    def _handle_scale_data(self, data: dict):
        self.ui.fx_lbl.setText(f"{data['x']:.2f}")
        self.ui.fy_lbl.setText(f"{data['y']:.2f}")
        self.ui.fz_lbl.setText(f"{data['z']:.2f}")
        self.ui.mx_lbl.setText(f"{data['mx']:.2f}")
        self.ui.my_lbl.setText(f"{data['my']:.2f}")
        self.ui.mz_lbl.setText(f"{data['mz']:.2f}")
        self.scale_chart.update_chart(data)
        
    def _handle_status_data(self, data: dict):
        self.ready = data['ready']
        self.moving = data['moving']
    
    def set_pitch(self, value: float):
        self.scales.set_pitch(value)

    def set_yaw(self, value: float):
        self.scales.set_yaw(value)

    def set_roll(self, value: float):
        self.scales.set_roll(value)

    def set_parameters(self, pitch: float, roll: float, yaw: float):
        self.scales.set_pitch_yaw_roll(pitch, yaw, roll)

    def start_test_plan(self):
        Thread(target=self._run_test_plan, daemon=True).start()

    def _run_test_plan(self):
        test_plan = self.test_plan_wg.get_test_plan()
        self.test_plan_wg.show_message(True)
        for row in test_plan:
            self._wait_until(add_sec_to_current_time(row[0]))

            if self.stop_plan:
                self.stop_plan = False
                break

            self.set_parameters(row[1], row[2], row[3])

        self.test_plan_wg.show_message(False)

    def _wait_until(self, target_time: datetime):
        while datetime.now() < target_time and not self.stop_plan:
            sleep(0.1)

    def _stop_plan(self):
        self.stop_plan = True