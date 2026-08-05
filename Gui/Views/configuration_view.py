from datetime import datetime
from threading import Thread
from time import sleep
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Device_controllers.papago_controller import PapagoController
from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Gui.Charts.zoomable_chart import ZoomableChart
from Gui.Custom_functions.test_plan_tab import TestPlanTab
from Qt_files.Qt_python.ui_wind_tunnel_config_view import Ui_Form
from Utils.static_methods import add_sec_to_current_time


class ConfigurationView(QWidget):
    RETURN_TO_MAIN = Signal()

    def __init__(self, plc: TunnelPLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tunnel_plc = plc
        self.papago = papago

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
        self.tunnel_plc.PLC_DATA.connect(self._handle_plc_data)

    def _start_test_plan(self):
        Thread(target=self._run_test_plan, daemon=True).start()

    # todo: add disabling tunnel control buttons while test plan is running
    # todo: need to set control byte
    def _run_test_plan(self):
        test_plan = self.test_plan_wg.get_test_plan()
        self.test_plan_wg.show_message(True)
        for row in test_plan:
            self._wait_until(add_sec_to_current_time(row[0]))
            pid = True if row[1] != "" else False

            if self.stop_plan:
                self.stop_plan = False
                break

            if pid:
                self.tunnel_plc.set_wind_velocity(row[1])
            else:
                self.tunnel_plc.set_engine_frequency(row[2])

        self.test_plan_wg.show_message(False)
    
    def _stop_test_plan(self):
        self.stop_plan = True

    def _handle_plc_data(self, plc_data: dict):
        self.chart.update_chart([plc_data.get("wind_filtered"), plc_data.get("average_temp")])

    def _wait_until(self, target_time: datetime):
        while datetime.now() < target_time and not self.stop_plan:
            sleep(0.1)
