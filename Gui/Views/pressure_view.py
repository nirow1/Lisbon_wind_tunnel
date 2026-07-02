from PySide6.QtWidgets import QWidget

from Gui.Charts.zoomable_chart import ZoomableChart
from Qt_files.Qt_python.ui_wind_tunnel_pressure_view import Ui_Form


class PressureView(QWidget):
    def __init__(self, tlaskan_1, tlaskan_2):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tlaskan_1 = tlaskan_1
        self.tlaskan_2 = tlaskan_2

        self.pressure_chart_1 = ZoomableChart("pressure 1",
                                              x_axis_seconds=600,
                                              y_axis=(-500, 500),
                                              line_name=[f"P{i}" for i in range(1,17)],
                                              line_count=16)
        self.ui.pressure_chart_lo.addWidget(self.pressure_chart_1)

        self.pressure_chart_2 = ZoomableChart("pressure 2",
                                              x_axis_seconds=600,
                                              y_axis=(-500, 500),
                                              line_name=[f"P{i}" for i in range(1,17)],
                                              line_count=16)
        self.ui.pressure_chart_lo_2.addWidget(self.pressure_chart_2)

        self._bind_buttons()
        self._bind_emits()
        self._initial_graphical_changes()

    def _initial_graphical_changes(self):
        pass

    def _bind_buttons(self):
        self.ui.page_1_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page))
        self.ui.page_2_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_2))

        self.ui.reset_pressure_chart_btn.clicked.connect(self.pressure_chart_1.reset_axis)
        self.ui.reset_pressure_chart_btn_2.clicked.connect(self.pressure_chart_2.reset_axis)

    def _bind_emits(self):
        pass