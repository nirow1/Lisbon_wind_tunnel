from PySide6.QtWidgets import QWidget

from Gui.Charts.zoomable_chart import ZoomableChart
from Qt_files.Qt_python.ui_wind_tunnel_scale_view import Ui_Form


class ScaleView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.scale_chart = ZoomableChart("Balances",
                                              x_axis_seconds=600,
                                              y_axis=(-500, 500),
                                              line_name=["Fx","Fy","fz","","",""],
                                              line_count=6)
        self.ui.scale_chart.addWidget(self.scale_chart)

        self._bind_buttons()
        self._bind_emits()
        self._initial_graphical_changes()

    def _initial_graphical_changes(self):
        pass

    def _bind_buttons(self):
        pass

    def _bind_emits(self):
        pass