from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Device_controllers.papago_controller import PapagoController
from Device_controllers.tunnel_plc_controller import TunnelPLCController
from Gui.Charts.zoomable_chart import ZoomableChart
from Qt_files.Qt_python.ui_wind_tunnel_config_view import Ui_Form


class ConfigurationView(QWidget):
    RETURN_TO_MAIN = Signal()

    def __init__(self, plc: TunnelPLCController, papago: PapagoController):
        QWidget.__init__(self)
        self.concentric: bool = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tunnel_plc = plc
        self.papago = papago

        self._init_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _init_graphical_changes(self):
        # charts setup block
        self.chart = ZoomableChart(
            name="",
            x_axis_seconds=600,
            y_axis=(0, 50),
            line_name=["Wind velocity[m/s]", "Wind temperature [°C]"],
            line_count=2
        )

        self.ui.scale_chart.addWidget(self.chart)

    def _bind_buttons(self):
        # saving handling
        self.ui.restart_chart_btn.clicked.connect(self.chart.reset_axis)

        self.ui.chart_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))
        self.ui.test_plan_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.test_plan_pg))

    def _bind_emits(self):
        self.tunnel_plc.PLC_DATA.connect(self._handle_plc_data)

    def _handle_plc_data(self, plc_data: dict):
        self.chart.update_chart([plc_data.get("wind_filtered"), plc_data.get("average_temp")])
