# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Brest_wind_tunnelkouIDL.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1380, 857)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"QSlider{ margin: 0px;}\n"
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
"#widget_200, #widget_201, #widget_202, #widget_203, #widget_204,\n"
"#widget_205, #widget_206, #widget_207, #widget_208, #widget_209,\n"
" #tableWidget {\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.widget_19 = QWidget(self.centralwidget)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_200 = QWidget(self.widget_19)
        self.widget_200.setObjectName(u"widget_200")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_200.sizePolicy().hasHeightForWidth())
        self.widget_200.setSizePolicy(sizePolicy)
        self.widget_200.setMinimumSize(QSize(0, 550))
        self.widget_200.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_200)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, -1, 3, 3)
        self.widget_3 = QWidget(self.widget_200)
        self.widget_3.setObjectName(u"widget_3")
        self.control_panel_lo = QHBoxLayout(self.widget_3)
        self.control_panel_lo.setSpacing(0)
        self.control_panel_lo.setObjectName(u"control_panel_lo")
        self.control_panel_lo.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_16.addWidget(self.widget_200)

        self.widget_201 = QWidget(self.widget_19)
        self.widget_201.setObjectName(u"widget_201")
        self.verticalLayout_5 = QVBoxLayout(self.widget_201)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, -1, 3, 3)
        self.widget_202 = QWidget(self.widget_201)
        self.widget_202.setObjectName(u"widget_202")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_202.sizePolicy().hasHeightForWidth())
        self.widget_202.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.widget_202)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, -1, 1, 1)
        self.widget = QWidget(self.widget_202)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.config_pg_btn = QPushButton(self.widget)
        self.config_pg_btn.setObjectName(u"config_pg_btn")
        self.config_pg_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.config_pg_btn)

        self.run_pg_btn = QPushButton(self.widget)
        self.run_pg_btn.setObjectName(u"run_pg_btn")
        self.run_pg_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.run_pg_btn)

        self.next_params_pg_btn = QPushButton(self.widget)
        self.next_params_pg_btn.setObjectName(u"next_params_pg_btn")
        self.next_params_pg_btn.setMinimumSize(QSize(0, 30))
        self.next_params_pg_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.next_params_pg_btn)

        self.pid_settings_pg_btn = QPushButton(self.widget)
        self.pid_settings_pg_btn.setObjectName(u"pid_settings_pg_btn")
        self.pid_settings_pg_btn.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_3.addWidget(self.pid_settings_pg_btn)


        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_202)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.wind_vel_pg = QWidget()
        self.wind_vel_pg.setObjectName(u"wind_vel_pg")
        self.verticalLayout_12 = QVBoxLayout(self.wind_vel_pg)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, -1, 2, -1)
        self.widget_18 = QWidget(self.wind_vel_pg)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy1.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy1)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.widget_38 = QWidget(self.widget_18)
        self.widget_38.setObjectName(u"widget_38")
        self.scale_chart = QGridLayout(self.widget_38)
        self.scale_chart.setObjectName(u"scale_chart")
        self.scale_chart.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_38)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 40))
        self.widget_4.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout.addWidget(self.widget_6)

        self.restart_chart_btn = QPushButton(self.widget_4)
        self.restart_chart_btn.setObjectName(u"restart_chart_btn")
        self.restart_chart_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.restart_chart_btn)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777, 16777215))

        self.horizontalLayout.addWidget(self.widget_8)


        self.scale_chart.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_38)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")

        self.horizontalLayout_8.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.start_tunnel_btn = QPushButton(self.widget_9)
        self.start_tunnel_btn.setObjectName(u"start_tunnel_btn")
        self.start_tunnel_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_11.addWidget(self.start_tunnel_btn)

        self.widget_27 = QWidget(self.widget_9)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 44))
        self.widget_27.setMaximumSize(QSize(125, 16777215))
        self.widget_27.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #FF3636;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF2626;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stop_tunnel_btn = QPushButton(self.widget_27)
        self.stop_tunnel_btn.setObjectName(u"stop_tunnel_btn")
        self.stop_tunnel_btn.setEnabled(False)
        self.stop_tunnel_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_10.addWidget(self.stop_tunnel_btn)


        self.horizontalLayout_11.addWidget(self.widget_27)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.scale_chart.addWidget(self.widget_2, 0, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.widget_38)


        self.verticalLayout_12.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.wind_vel_pg)
        self.next_params_pg = QWidget()
        self.next_params_pg.setObjectName(u"next_params_pg")
        self.horizontalLayout_12 = QHBoxLayout(self.next_params_pg)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_10 = QWidget(self.next_params_pg)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_7.addWidget(self.label_9)

        self.widget_205 = QWidget(self.widget_10)
        self.widget_205.setObjectName(u"widget_205")
        self.verticalLayout_8 = QVBoxLayout(self.widget_205)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_13 = QWidget(self.widget_205)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_13.addWidget(self.label_14)

        self.temp_in_raw_lbl = QLabel(self.widget_13)
        self.temp_in_raw_lbl.setObjectName(u"temp_in_raw_lbl")
        self.temp_in_raw_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.temp_in_raw_lbl)

        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)


        self.verticalLayout_8.addWidget(self.widget_13)

        self.widget_28 = QWidget(self.widget_205)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_28)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_14.addWidget(self.label_17)

        self.temp_out_raw_lbl = QLabel(self.widget_28)
        self.temp_out_raw_lbl.setObjectName(u"temp_out_raw_lbl")
        self.temp_out_raw_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.temp_out_raw_lbl)

        self.label_19 = QLabel(self.widget_28)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)


        self.verticalLayout_8.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_205)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_29)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_15.addWidget(self.label_20)

        self.diff_pres_raw_lbl = QLabel(self.widget_29)
        self.diff_pres_raw_lbl.setObjectName(u"diff_pres_raw_lbl")
        self.diff_pres_raw_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.diff_pres_raw_lbl)

        self.label_22 = QLabel(self.widget_29)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)


        self.verticalLayout_8.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_205)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_30)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_17.addWidget(self.label_23)

        self.diff_pres_fltr_lbl = QLabel(self.widget_30)
        self.diff_pres_fltr_lbl.setObjectName(u"diff_pres_fltr_lbl")
        self.diff_pres_fltr_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.diff_pres_fltr_lbl)

        self.label_25 = QLabel(self.widget_30)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)


        self.verticalLayout_8.addWidget(self.widget_30)


        self.verticalLayout_7.addWidget(self.widget_205)

        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_7.addWidget(self.label_11)

        self.widget_206 = QWidget(self.widget_10)
        self.widget_206.setObjectName(u"widget_206")
        self.gridLayout = QGridLayout(self.widget_206)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_32 = QWidget(self.widget_206)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.widget_32)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_19.addWidget(self.label_29)

        self.driver_status_lbl = QLabel(self.widget_32)
        self.driver_status_lbl.setObjectName(u"driver_status_lbl")
        self.driver_status_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.driver_status_lbl)

        self.label_31 = QLabel(self.widget_32)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_19.addWidget(self.label_31)


        self.gridLayout.addWidget(self.widget_32, 0, 0, 1, 1)

        self.widget_34 = QWidget(self.widget_206)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.widget_34)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_21.addWidget(self.label_35)

        self.output_lbl = QLabel(self.widget_34)
        self.output_lbl.setObjectName(u"output_lbl")
        self.output_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_21.addWidget(self.output_lbl)

        self.label_37 = QLabel(self.widget_34)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_21.addWidget(self.label_37)


        self.gridLayout.addWidget(self.widget_34, 2, 0, 1, 1)

        self.widget_33 = QWidget(self.widget_206)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_33)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_20.addWidget(self.label_32)

        self.current_lbl = QLabel(self.widget_33)
        self.current_lbl.setObjectName(u"current_lbl")
        self.current_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_20.addWidget(self.current_lbl)

        self.label_34 = QLabel(self.widget_33)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_20.addWidget(self.label_34)


        self.gridLayout.addWidget(self.widget_33, 3, 0, 1, 1)

        self.widget_31 = QWidget(self.widget_206)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_31)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_18.addWidget(self.label_26)

        self.error_code_lbl = QLabel(self.widget_31)
        self.error_code_lbl.setObjectName(u"error_code_lbl")
        self.error_code_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.error_code_lbl)

        self.label_28 = QLabel(self.widget_31)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_18.addWidget(self.label_28)


        self.gridLayout.addWidget(self.widget_31, 1, 0, 1, 1)

        self.widget_39 = QWidget(self.widget_206)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_39)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_26.addWidget(self.label_47)

        self.moment_lbl = QLabel(self.widget_39)
        self.moment_lbl.setObjectName(u"moment_lbl")
        self.moment_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_26.addWidget(self.moment_lbl)

        self.label_49 = QLabel(self.widget_39)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_26.addWidget(self.label_49)


        self.gridLayout.addWidget(self.widget_39, 0, 1, 1, 1)

        self.widget_36 = QWidget(self.widget_206)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_36)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_24.addWidget(self.label_41)

        self.converter_temp_lbl = QLabel(self.widget_36)
        self.converter_temp_lbl.setObjectName(u"converter_temp_lbl")
        self.converter_temp_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_24.addWidget(self.converter_temp_lbl)

        self.label_43 = QLabel(self.widget_36)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_24.addWidget(self.label_43)


        self.gridLayout.addWidget(self.widget_36, 2, 1, 1, 1)

        self.widget_37 = QWidget(self.widget_206)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_37)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_25.addWidget(self.label_44)

        self.engine_temp_lbl = QLabel(self.widget_37)
        self.engine_temp_lbl.setObjectName(u"engine_temp_lbl")
        self.engine_temp_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.engine_temp_lbl)

        self.label_46 = QLabel(self.widget_37)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_25.addWidget(self.label_46)


        self.gridLayout.addWidget(self.widget_37, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_206)

        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_7.addWidget(self.label_12)

        self.widget_207 = QWidget(self.widget_10)
        self.widget_207.setObjectName(u"widget_207")
        self.gridLayout_2 = QGridLayout(self.widget_207)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_40 = QWidget(self.widget_207)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.widget_40)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(170, 0))
        self.label_74.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_36.addWidget(self.label_74)

        self.est_converter_ld = QLabel(self.widget_40)
        self.est_converter_ld.setObjectName(u"est_converter_ld")
        self.est_converter_ld.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_36.addWidget(self.est_converter_ld)

        self.label_76 = QLabel(self.widget_40)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_36.addWidget(self.label_76)


        self.gridLayout_2.addWidget(self.widget_40, 0, 0, 1, 1)

        self.widget_44 = QWidget(self.widget_207)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.widget_44)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_40.addWidget(self.label_86)

        self.est_hexapod_ld = QLabel(self.widget_44)
        self.est_hexapod_ld.setObjectName(u"est_hexapod_ld")
        self.est_hexapod_ld.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_40.addWidget(self.est_hexapod_ld)

        self.label_88 = QLabel(self.widget_44)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_40.addWidget(self.label_88)


        self.gridLayout_2.addWidget(self.widget_44, 0, 1, 1, 1)

        self.widget_35 = QWidget(self.widget_207)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.widget_35)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(170, 0))
        self.label_71.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_35.addWidget(self.label_71)

        self.est_service_ld = QLabel(self.widget_35)
        self.est_service_ld.setObjectName(u"est_service_ld")
        self.est_service_ld.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_35.addWidget(self.est_service_ld)

        self.label_73 = QLabel(self.widget_35)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_35.addWidget(self.label_73)


        self.gridLayout_2.addWidget(self.widget_35, 1, 0, 1, 1)

        self.widget_43 = QWidget(self.widget_207)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.widget_43)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_39.addWidget(self.label_83)

        self.est_doors_meas_space_ld = QLabel(self.widget_43)
        self.est_doors_meas_space_ld.setObjectName(u"est_doors_meas_space_ld")
        self.est_doors_meas_space_ld.setMaximumSize(QSize(25, 26))

        self.horizontalLayout_39.addWidget(self.est_doors_meas_space_ld)

        self.label_85 = QLabel(self.widget_43)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_39.addWidget(self.label_85)


        self.gridLayout_2.addWidget(self.widget_43, 1, 1, 1, 1)

        self.widget_42 = QWidget(self.widget_207)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.widget_42)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(170, 0))
        self.label_80.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_38.addWidget(self.label_80)

        self.est_measure_space_ld = QLabel(self.widget_42)
        self.est_measure_space_ld.setObjectName(u"est_measure_space_ld")
        self.est_measure_space_ld.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_38.addWidget(self.est_measure_space_ld)

        self.label_82 = QLabel(self.widget_42)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_38.addWidget(self.label_82)


        self.gridLayout_2.addWidget(self.widget_42, 2, 0, 1, 1)

        self.widget_46 = QWidget(self.widget_207)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_42 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.widget_46)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_42.addWidget(self.label_92)

        self.est_doors_meas_space_ld_2 = QLabel(self.widget_46)
        self.est_doors_meas_space_ld_2.setObjectName(u"est_doors_meas_space_ld_2")
        self.est_doors_meas_space_ld_2.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_42.addWidget(self.est_doors_meas_space_ld_2)

        self.label_94 = QLabel(self.widget_46)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_42.addWidget(self.label_94)


        self.gridLayout_2.addWidget(self.widget_46, 2, 1, 1, 1)

        self.widget_41 = QWidget(self.widget_207)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.widget_41)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(170, 0))
        self.label_77.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_37.addWidget(self.label_77)

        self.est_entry_doors_ld = QLabel(self.widget_41)
        self.est_entry_doors_ld.setObjectName(u"est_entry_doors_ld")
        self.est_entry_doors_ld.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_37.addWidget(self.est_entry_doors_ld)

        self.label_79 = QLabel(self.widget_41)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_37.addWidget(self.label_79)


        self.gridLayout_2.addWidget(self.widget_41, 3, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_207)


        self.horizontalLayout_12.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.next_params_pg)
        self.login_pg = QWidget()
        self.login_pg.setObjectName(u"login_pg")
        self.pressure_chart_la = QVBoxLayout(self.login_pg)
        self.pressure_chart_la.setObjectName(u"pressure_chart_la")
        self.pressure_chart_la.setContentsMargins(3, 3, 3, 3)
        self.widget_23 = QWidget(self.login_pg)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_204 = QWidget(self.widget_23)
        self.widget_204.setObjectName(u"widget_204")
        self.widget_204.setMaximumSize(QSize(400, 200))
        self.verticalLayout_3 = QVBoxLayout(self.widget_204)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_24 = QWidget(self.widget_204)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.widget_24)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.user_name_le = QLineEdit(self.widget_24)
        self.user_name_le.setObjectName(u"user_name_le")
        self.user_name_le.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.user_name_le)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_204)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.widget_25)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.password_le = QLineEdit(self.widget_25)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_6.addWidget(self.password_le)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_204)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.log_in_btn = QPushButton(self.widget_26)
        self.log_in_btn.setObjectName(u"log_in_btn")
        self.log_in_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.log_in_btn)


        self.verticalLayout_3.addWidget(self.widget_26)


        self.horizontalLayout_5.addWidget(self.widget_204)


        self.pressure_chart_la.addWidget(self.widget_23)

        self.stackedWidget.addWidget(self.login_pg)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.widget_49 = QWidget(self.widget_202)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.widget_20 = QWidget(self.widget_49)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(130, 0))
        self.widget_20.setStyleSheet(u"QWidget{\n"
"	\n"
"}\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: #ccc;\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: rgb(230, 230, 230);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_33.addWidget(self.widget_20)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer)

        self.j4_logo_lbl = QLabel(self.widget_49)
        self.j4_logo_lbl.setObjectName(u"j4_logo_lbl")
        self.j4_logo_lbl.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_33.addWidget(self.j4_logo_lbl)


        self.verticalLayout_6.addWidget(self.widget_49)


        self.verticalLayout_5.addWidget(self.widget_202)


        self.horizontalLayout_16.addWidget(self.widget_201)


        self.verticalLayout_4.addWidget(self.widget_19)

        self.widget_203 = QWidget(self.centralwidget)
        self.widget_203.setObjectName(u"widget_203")
        self.widget_203.setMinimumSize(QSize(50, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_203)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.widget_11 = QWidget(self.widget_203)
        self.widget_11.setObjectName(u"widget_11")

        self.horizontalLayout_2.addWidget(self.widget_11)

        self.label_2 = QLabel(self.widget_203)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.led_1 = QLabel(self.widget_203)
        self.led_1.setObjectName(u"led_1")
        self.led_1.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_1)

        self.widget_22 = QWidget(self.widget_203)
        self.widget_22.setObjectName(u"widget_22")

        self.horizontalLayout_2.addWidget(self.widget_22)

        self.label_13 = QLabel(self.widget_203)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.led_6 = QLabel(self.widget_203)
        self.led_6.setObjectName(u"led_6")
        self.led_6.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_6)

        self.widget_12 = QWidget(self.widget_203)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout_2.addWidget(self.widget_12)

        self.label_4 = QLabel(self.widget_203)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.led_2 = QLabel(self.widget_203)
        self.led_2.setObjectName(u"led_2")
        self.led_2.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_2)

        self.widget_15 = QWidget(self.widget_203)
        self.widget_15.setObjectName(u"widget_15")

        self.horizontalLayout_2.addWidget(self.widget_15)

        self.label_6 = QLabel(self.widget_203)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.led_3 = QLabel(self.widget_203)
        self.led_3.setObjectName(u"led_3")
        self.led_3.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_3)

        self.widget_17 = QWidget(self.widget_203)
        self.widget_17.setObjectName(u"widget_17")

        self.horizontalLayout_2.addWidget(self.widget_17)

        self.label_10 = QLabel(self.widget_203)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.led_5 = QLabel(self.widget_203)
        self.led_5.setObjectName(u"led_5")
        self.led_5.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_5)

        self.widget_21 = QWidget(self.widget_203)
        self.widget_21.setObjectName(u"widget_21")

        self.horizontalLayout_2.addWidget(self.widget_21)

        self.label_3 = QLabel(self.widget_203)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.led_7 = QLabel(self.widget_203)
        self.led_7.setObjectName(u"led_7")
        self.led_7.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_7)

        self.widget_16 = QWidget(self.widget_203)
        self.widget_16.setObjectName(u"widget_16")

        self.horizontalLayout_2.addWidget(self.widget_16)

        self.label_8 = QLabel(self.widget_203)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.led_4 = QLabel(self.widget_203)
        self.led_4.setObjectName(u"led_4")
        self.led_4.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.led_4)

        self.widget_14 = QWidget(self.widget_203)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout_2.addWidget(self.widget_14)


        self.verticalLayout_4.addWidget(self.widget_203)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.config_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.run_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.next_params_pg_btn.setText(QCoreApplication.translate("MainWindow", u"Next parameters", None))
        self.pid_settings_pg_btn.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.restart_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Reset chart axis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Velocity [m/s]", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ferequency [Hz]", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ramp on", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ramp down [s]", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ramp up [s]", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Run duration [s]", None));
        self.start_tunnel_btn.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.stop_tunnel_btn.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Measurements", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Temperature input RAW:", None))
        self.temp_in_raw_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Temperature output RAW:", None))
        self.temp_out_raw_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Differencial pressure RAW:", None))
        self.diff_pres_raw_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Pa", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Differencial pressure filtered:", None))
        self.diff_pres_fltr_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pa", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fan", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Driver status:", None))
        self.driver_status_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_31.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Power output:", None))
        self.output_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.current_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Error code:", None))
        self.error_code_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_28.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Momnent:", None))
        self.moment_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Nm", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Converter temperature:", None))
        self.converter_temp_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Engine temperature:", None))
        self.engine_temp_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Safety circuits", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"E-stop switchboard:", None))
        self.est_converter_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_76.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"E-stop hexapod:", None))
        self.est_hexapod_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_88.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"E-stop service:", None))
        self.est_service_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_73.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Doors test section:", None))
        self.est_doors_meas_space_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_85.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"E-stop test section:", None))
        self.est_measure_space_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_82.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Doors test section:", None))
        self.est_doors_meas_space_ld_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_94.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"E-stop entry doors", None))
        self.est_entry_doors_ld.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_79.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.log_in_btn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.j4_logo_lbl.setText(QCoreApplication.translate("MainWindow", u"4J Logo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ready", None))
        self.led_1.setText(QCoreApplication.translate("MainWindow", u"L1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"e-reset", None))
        self.led_6.setText(QCoreApplication.translate("MainWindow", u"L6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"e-stop", None))
        self.led_2.setText(QCoreApplication.translate("MainWindow", u"L2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"doors", None))
        self.led_3.setText(QCoreApplication.translate("MainWindow", u"L3", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"drive error", None))
        self.led_5.setText(QCoreApplication.translate("MainWindow", u"L5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"concetrc", None))
        self.led_7.setText(QCoreApplication.translate("MainWindow", u"L7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"surge protection", None))
        self.led_4.setText(QCoreApplication.translate("MainWindow", u"L4", None))
    # retranslateUi

