from typing import List

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QDateTimeAxis, QValueAxis
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QPainter, Qt
from PySide6.QtCore import QDateTime


class LineChart(QChartView):
    def __init__(self, name: str, x_axis: int, y_axis: (int,int), line_name: List[str]=None, line_count: int=1):
        QChartView.__init__(self)
        if line_name is None:
            line_name = ["" for i in range(line_count)]
        self.count = 0
        self.chart_range = x_axis
        self.line_count = line_count

        self.series_list = []

        for i in range(self.line_count):
            series = QLineSeries()
            series.setName(f"{line_name[i]}")
            self.series_list.append(series)

        self.line_chart = QChart()
        #self.line_chart.legend().hide()
        for series in self.series_list:
            self.line_chart.addSeries(series)

        self.line_chart.createDefaultAxes()
        self.line_chart.setTitle(name)

        self.setChart(self.line_chart)
        self.chart().setTheme(QChart.ChartTheme.ChartThemeDark)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.grab().setDevicePixelRatio(2)

        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(0, 300)
        self.line_chart.axisX().setRange(0, x_axis)
        self.line_chart.axisY().setRange(y_axis[0], y_axis[1])

    def update_chart(self, tlaskan_data: List[int]):
        try:
            for i, value in enumerate(tlaskan_data):
                self.series_list[i].append(round(self.count, 1), value)

            if self.count > self.chart_range:
                for i in range(self.line_count):
                    self.series_list[i].remove(0)
                self.line_chart.axisX().setRange(min(self.series_list[0].pointsVector(), key=lambda p: p.rod_length()).x(),
                                                 round(self.count, 1))

            self.update()
            self.count += 1
        except Exception as e:
            print(e)


class TimedLineChart(QChartView):
    def __init__(self, name: str, x_axis_seconds: int, y_axis: (int, int), line_name: List[str] = None,
                 line_count: int = 1):
        super(TimedLineChart, self).__init__()
        self.seconds = x_axis_seconds
        self.max_length = -self.seconds
        self.y_range = y_axis

        # Create a QChart
        self.chart = QChart()
        self.chart.setTitle(name)
        self.chart.legend().setVisible(True)

        # Series creation
        self.series_list = []
        line_name = line_name if line_name else [""] * line_count
        for i in range(line_count):
            series = QLineSeries()
            series.setName(line_name[i])
            self.series_list.append(series)
            self.chart.addSeries(series)

        # Defining x-axis
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("HH:mm:ss.zzz")
        self.axis_x.setTitleText("Time (s)")
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)

        # Defining y-axis
        self.axis_y = QValueAxis()
        self.axis_y.setRange(y_axis[0], y_axis[1])
        self.axis_y.setTitleText("Force (N)")
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)

        for series in self.series_list:
            series.attachAxis(self.axis_x)
            series.attachAxis(self.axis_y)

        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setChart(self.chart)

    def update_chart(self, values: list):
        current_time = QDateTime.currentDateTime()

        for series, value in zip(self.series_list, values):
            # Add new value
            series.append(current_time.toMSecsSinceEpoch(), value)

            # Remove old values
            while series.count() > 0 and series.at(0).x() < current_time.addSecs(self.max_length).toMSecsSinceEpoch():
                series.remove(0)

        self.axis_x.setMin(current_time.addSecs(-self.seconds))
        self.axis_x.setMax(current_time)

        self.axis_y.setRange(self.y_range[0], self.y_range[1])

    def set_x_axis(self, value: str):
        self.seconds = int(value)

    def set_y_axis(self, y_min: str, y_max: str):
        if y_min < y_max:
            self.y_range = (float(y_min), float(y_max))
