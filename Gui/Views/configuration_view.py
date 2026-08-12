from datetime import datetime, timezone
from threading import Thread
from time import sleep

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Gui.Charts.zoomable_chart import ZoomableChart
from Gui.Custom_functions.test_plan_tab import TestPlanTab
from Qt_files.Qt_python.ui_wind_tunnel_config_view import Ui_Form
from Utils.static_methods import add_sec_to_current_time


class ConfigurationView(QWidget):
    RETURN_TO_MAIN = Signal()
    TEST_RUNNING = Signal(bool)

    def __init__(self, plc: TunnelPLCController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tunnel_plc = plc

        # charts setup block
        self.chart = ZoomableChart(
            name="",
            x_axis_seconds=600,
            y_axis=(0, 50),
            line_name=["Wind velocity[m/s]", "Wind temperature [°C]"],
            line_count=2
        )
        self.ui.scale_chart.addWidget(self.chart)

        self.test_plan_wg = TestPlanTab(["Velocity [m/s]", "Frequency [Hz]"])
        self.ui.test_plan_vl.addWidget(self.test_plan_wg)
        self.stop_plan = False

        self._init_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _init_graphical_changes(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg)

    def _bind_buttons(self):
        # saving handling
        self.ui.restart_chart_btn.clicked.connect(self.chart.reset_axis)

        self.ui.chart_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))
        self.ui.test_plan_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.test_plan_pg))

        self.test_plan_wg.ui.start_test_plan_btn.clicked.connect(self._start_test_plan)
        self.test_plan_wg.ui.stop_test_plan_btn.clicked.connect(self._stop_test_plan)

    def _bind_emits(self):
        self.tunnel_plc.SENSOR_VALUES.connect(self._handle_plc_data)

    def _start_test_plan(self):
        Thread(target=self._run_test_plan, daemon=True).start()

    def _run_test_plan(self):
        test_plan = self.test_plan_wg.get_test_plan()
        self.TEST_RUNNING.emit(True)
        self.test_plan_wg.show_message(True)
        self.tunnel_plc.start_engine()
        for row in test_plan:
            self._wait_until(add_sec_to_current_time(row[0]))

            if self.stop_plan:
                self.stop_plan = False
                break

            # velocity set → PID regulation (False); frequency set → frequency mode (True)
            # switch_pid only updates the local control byte; start_engine writes it to the PLC
            use_frequency = row[1] == ""
            self.tunnel_plc.switch_pid(use_frequency)
            if use_frequency:
                self.tunnel_plc.set_engine_frequency(row[2])
            else:
                self.tunnel_plc.set_wind_velocity(row[1])

        # same main PLC shutdown steps as InfoView.stop_tunnel
        # (velocity/frequency zeroing is handled inside stop_engine)
        self.tunnel_plc.switch_pid(False)
        self.tunnel_plc.stop_engine()
        self.test_plan_wg.show_message(False)
        self.TEST_RUNNING.emit(False)
    
    def _stop_test_plan(self):
        self.stop_plan = True

    def _handle_plc_data(self, plc_data: dict):
        self.chart.update_chart([plc_data.get("speed"), plc_data.get("average_temp")])

    def _wait_until(self, target_time: datetime):
        while datetime.now(timezone.utc) < target_time and not self.stop_plan:
            sleep(0.1)
