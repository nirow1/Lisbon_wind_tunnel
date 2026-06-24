from PySide6.QtCharts import QLineSeries, QChart, QChartView, QDateTimeAxis, QValueAxis
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QPainter, Qt
from PySide6 import QtCore
from typing import List, Tuple


class ZoomableChart(QChartView):
    def __init__(self, name: str, x_axis_seconds: int, y_axis: Tuple[int, int], line_name: List[str] = None,
                 line_count: int = 1):
        super().__init__()
        self.chart = QChart()
        self.chart.setTitle(name)
        self.chart.legend().setVisible(True)
        self.setChart(self.chart)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.follow_mode = True

        # Create a sample line series
        self.series_list = []
        line_name = line_name if line_name else [""] * line_count
        for i in range(line_count):
            series = QLineSeries()
            series.setName(line_name[i])
            self.series_list.append(series)
            self.chart.addSeries(series)


        self.seconds = x_axis_seconds
        self.max_length = -self.seconds

        # Set up axes
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("HH:mm:ss")
        self.axis_x.setTitleText("Time (s)")
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(y_axis[0], y_axis[1])
        self.axis_y.setTitleText("Value")
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.y_axis_range = (y_axis[0], y_axis[1])

        for series in self.series_list:
            series.attachAxis(self.axis_x)
            series.attachAxis(self.axis_y)

        self.setRubberBand(QChartView.RubberBand.RectangleRubberBand)  # Enable selection-based zooming

    def wheelEvent(self, event):
        self.follow_mode = False
        factor = 1.1 if event.angleDelta().y() > 0 else 0.9  # Zoom in/out based on scroll direction
        self.chart.zoom(factor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.follow_mode = False
            self.last_mouse_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            delta = event.pos() - self.last_mouse_pos
            self.chart.scroll(-delta.x(), delta.y())
            self.last_mouse_pos = event.pos()

    def update_chart(self, values: list):
        current_time = QDateTime.currentDateTime()

        for series, value in zip(self.series_list, values):
            series.append(current_time.toMSecsSinceEpoch(), value)
            while series.count() > 0 and series.at(0).x() < current_time.addSecs(self.max_length).toMSecsSinceEpoch():
                series.remove(0)

        if self.follow_mode:  # only move X axis in follow mode
            min_time = current_time.addSecs(-self.seconds)
            self.axis_x.setRange(min_time, current_time)

    def reset_axis(self):
        self.follow_mode = True
        self.axis_y.setRange(self.y_axis_range[0], self.y_axis_range[1])
