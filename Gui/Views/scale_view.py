from datetime import datetime
from threading import Thread
from time import sleep

from PySide6.QtWidgets import QWidget

from Gui.Charts.zoomable_chart import ZoomableChart
from Gui.Custom_functions.test_plan_tab import TestPlanTab
from Qt_files.Qt_python.ui_wind_tunnel_scale_view import Ui_Form
from Utils.static_methods import add_sec_to_current_time


class ScaleView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stop_plan = False

        self.scale_chart = ZoomableChart("Balances",
                                              x_axis_seconds=600,
                                              y_axis=(-500, 500),
                                              line_name=["Fx","Fy","fz","","",""],
                                              line_count=6)
        self.ui.scale_chart.addWidget(self.scale_chart)

        self.test_plan_wg = TestPlanTab(["Pitch", "Roll", "Yaw"])
        self.ui.test_plan_lo.addWidget(self.test_plan_wg)

        self._bind_buttons()
        self._bind_emits()
        self._initial_graphical_changes()

    def _initial_graphical_changes(self):
        self.ui.stackedWidget.setCurrentWidget(self.scale_chart)
        self.test_plan_wg.show_message(False)

    # todo: add setting pitch roll and yaw individually
    def _bind_buttons(self):
        self.ui.test_plan_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.test_plan_pg))
        self.ui.chart_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))

        self.test_plan_wg.ui.start_test_plan_btn.clicked.connect(self.start_test_plan)
        self.test_plan_wg.ui.stop_test_plan_btn.clicked.connect(self._stop_plan)

    def _bind_emits(self):
        pass

    def set_pitch(self, value: float):
        ...

    def set_yaw(self, value: float):
        ...

    def set_roll(self, value: float):
        ...

    def set_parameters(self, pitch: float, roll: float, yaw: float):
        self.set_pitch(pitch)
        self.set_roll(roll)
        self.set_yaw(yaw)

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