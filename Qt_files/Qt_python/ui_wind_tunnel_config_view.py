# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_config_viewClKKYt.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalLayout_3 = QVBoxLayout(self.widget_205)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.test_running_wg_2 = QWidget(self.widget_205)
        self.test_running_wg_2.setObjectName(u"test_running_wg_2")
        self.test_running_wg_2.setMinimumSize(QSize(0, 25))
        self.test_running_wg_2.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.test_running_wg_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.test_running_wg_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.test_running_wg_2)

        self.tableWidget_3d = QTableWidget(self.widget_205)
        if (self.tableWidget_3d.columnCount() < 4):
            self.tableWidget_3d.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3d.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3d.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3d.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3d.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_3d.setObjectName(u"tableWidget_3d")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3d.sizePolicy().hasHeightForWidth())
        self.tableWidget_3d.setSizePolicy(sizePolicy)
        self.tableWidget_3d.setAutoScrollMargin(16)
        self.tableWidget_3d.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidget_3d.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget_3d.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_3.addWidget(self.tableWidget_3d)

        self.widget_10 = QWidget(self.widget_205)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.widget_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_3d_row_btn = QPushButton(self.widget_10)
        self.add_3d_row_btn.setObjectName(u"add_3d_row_btn")
        self.add_3d_row_btn.setMinimumSize(QSize(0, 0))
        self.add_3d_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.add_3d_row_btn)

        self.start_3d_test_plan_btn = QPushButton(self.widget_10)
        self.start_3d_test_plan_btn.setObjectName(u"start_3d_test_plan_btn")
        self.start_3d_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.start_3d_test_plan_btn)

        self.stop_3d_test_plan_btn = QPushButton(self.widget_10)
        self.stop_3d_test_plan_btn.setObjectName(u"stop_3d_test_plan_btn")
        self.stop_3d_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.stop_3d_test_plan_btn)

        self.delete_3d_row_btn = QPushButton(self.widget_10)
        self.delete_3d_row_btn.setObjectName(u"delete_3d_row_btn")
        self.delete_3d_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.delete_3d_row_btn)


        self.verticalLayout_3.addWidget(self.widget_10)


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
        self.label_8.setText(QCoreApplication.translate("Form", u"test running", None))
        ___qtablewidgetitem = self.tableWidget_3d.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem1 = self.tableWidget_3d.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Sek", None));
        ___qtablewidgetitem2 = self.tableWidget_3d.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"wind velocity [m/s]", None));
        ___qtablewidgetitem3 = self.tableWidget_3d.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Frequency [Hz]", None));
        self.add_3d_row_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.start_3d_test_plan_btn.setText(QCoreApplication.translate("Form", u"Start plan", None))
        self.stop_3d_test_plan_btn.setText(QCoreApplication.translate("Form", u"End plan", None))
        self.delete_3d_row_btn.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

