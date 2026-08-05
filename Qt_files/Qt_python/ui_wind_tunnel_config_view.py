# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_config_viewUoIFjr.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(955, 673)
        Form.setStyleSheet(u"QSlider{ margin: 0px;}\n"
"QSlider::groove:horizontal{\n"
"border-radius: 5px;\n"
"height: 10px;\n"
"margin: 0px;\n"
"}\n"
"QSlider::groove:horizontal:hover{ background-color: rgb(200, 200, 200)}\n"
"QSlider::handle:horizontal{\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin:0px;\n"
"border-radius: 5px;\n"
"background-color:#1FA808;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background-color: rgb(160,160,160);\n"
"border-radius: 3px;\n"
" }\n"
"QSlider::add-page:horizontal {\n"
"background-color: rgb(190,190,190);\n"
"border-radius: 2px;\n"
" }\n"
"\n"
"QWidget{\n"
"background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"font: 11pt \\\"Yu Gothic UI\\\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
""
                        "}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}\n"
"\n"
"#widget, #widget_5, #widget_3, #widget_4{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.vertical_shit = QVBoxLayout(self.widget_4)
        self.vertical_shit.setObjectName(u"vertical_shit")
        self.vertical_shit.setContentsMargins(3, 3, 3, 3)
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.chart_pg_btn = QPushButton(self.widget)
        self.chart_pg_btn.setObjectName(u"chart_pg_btn")
        self.chart_pg_btn.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.chart_pg_btn)

        self.test_plan_pg_btn = QPushButton(self.widget)
        self.test_plan_pg_btn.setObjectName(u"test_plan_pg_btn")
        self.test_plan_pg_btn.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.test_plan_pg_btn)


        self.vertical_shit.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.chart_pg = QWidget()
        self.chart_pg.setObjectName(u"chart_pg")
        self.scale_chart = QVBoxLayout(self.chart_pg)
        self.scale_chart.setObjectName(u"scale_chart")
        self.scale_chart.setContentsMargins(3, 3, 3, 3)
        self.widget_5 = QWidget(self.chart_pg)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.restart_chart_btn = QPushButton(self.widget_5)
        self.restart_chart_btn.setObjectName(u"restart_chart_btn")
        self.restart_chart_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.restart_chart_btn)


        self.scale_chart.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.chart_pg)
        self.test_plan_pg = QWidget()
        self.test_plan_pg.setObjectName(u"test_plan_pg")
        self.horizontalLayout_3 = QHBoxLayout(self.test_plan_pg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_205 = QWidget(self.test_plan_pg)
        self.widget_205.setObjectName(u"widget_205")
        self.test_plan_vl = QVBoxLayout(self.widget_205)
        self.test_plan_vl.setObjectName(u"test_plan_vl")
        self.test_plan_vl.setContentsMargins(3, 3, 3, 3)

        self.horizontalLayout_3.addWidget(self.widget_205)

        self.stackedWidget.addWidget(self.test_plan_pg)

        self.vertical_shit.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.chart_pg_btn.setText(QCoreApplication.translate("Form", u"Chart", None))
        self.test_plan_pg_btn.setText(QCoreApplication.translate("Form", u"Test Plan", None))
        self.restart_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart axis", None))
    # retranslateUi

