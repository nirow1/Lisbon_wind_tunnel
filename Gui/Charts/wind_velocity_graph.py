from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtGui import QPainter, QColor, Qt


class WindVelocityDonut(QChartView):
    def __init__(self):
        QChartView.__init__(self)
        self.setObjectName("speed_donut")
        donut_chart = self.chart()
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        donut_chart.legend().setVisible(False)
        donut_chart.setTitle("Velocity m/s")
        donut_chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        donut_chart.setBackgroundBrush(QColor("#fafafa"))

        min_size = 0.6
        max_size = 0.8

        self.donut = QPieSeries()
        self.donut.setPieStartAngle(220)
        self.donut.setPieEndAngle(500)

        value = 40

        self.current_velocity = QPieSlice(str(value), value)
        self.current_velocity.setBrush(QColor("#4CAF50"))
        self.current_velocity.setLabelVisible(True)
        self.current_velocity.setLabelColor(Qt.GlobalColor.white)
        self.current_velocity.setLabelPosition(QPieSlice.LabelPosition.LabelInsideTangential)
        self.top_velocity = QPieSlice("", value)
        self.top_velocity.setBrush(QColor("#d6d6d6"))
        self.top_velocity.setLabelVisible(True)
        self.top_velocity.setLabelColor(Qt.GlobalColor.white)
        self.top_velocity.setLabelPosition(QPieSlice.LabelPosition.LabelInsideTangential)

        self.donut.append(self.current_velocity)
        self.donut.append(self.top_velocity)
        size = (max_size - min_size) / 1
        self.donut.setHoleSize(min_size + 1 * size)
        self.donut.setPieSize(min_size + (1 + 1) * size)
        donut_chart.addSeries(self.donut)
        self.setChart(donut_chart)

    def set_wind_velocity(self, velocity):
        self.current_velocity.setValue(velocity)
        self.current_velocity.setLabel(str(velocity))
        self.top_velocity.setValue(80-velocity)

