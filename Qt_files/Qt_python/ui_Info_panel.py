# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Info_panelRGosED.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from Gui.Custom_widgets.toggle import AnimatedToggle

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 750)
        Form.setMaximumSize(QSize(600, 16777215))
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
"#widget_11, #widget_31, #widget_40, #widget_9, #widget_22, #widget_15, #widget_12, #temp_engine_lbl, #max_min_temp_lbl,#max_min_pressure_lbl, #pressure_lbl, #wind_velocity_lbl, #max_min_velocity_lbl,\n"
"#frequency_lbl{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(540, 0))
        self.widget.setMaximumSize(QSize(540, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, -1, 3, 3)
        self.widget_37 = QWidget(self.widget)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy)
        self.widget_37.setMinimumSize(QSize(0, 0))
        self.widget_37.setStyleSheet(u"QLabel {\n"
"    background-color: #FF3636;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_37)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.plc_not_connected_lbl = QLabel(self.widget_37)
        self.plc_not_connected_lbl.setObjectName(u"plc_not_connected_lbl")
        self.plc_not_connected_lbl.setMinimumSize(QSize(0, 25))
        self.plc_not_connected_lbl.setMaximumSize(QSize(16777215, 25))
        self.plc_not_connected_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.plc_not_connected_lbl)

        self.reserved_error_lbl = QLabel(self.widget_37)
        self.reserved_error_lbl.setObjectName(u"reserved_error_lbl")
        self.reserved_error_lbl.setMinimumSize(QSize(0, 25))
        self.reserved_error_lbl.setMaximumSize(QSize(16777215, 25))
        self.reserved_error_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.reserved_error_lbl)


        self.verticalLayout.addWidget(self.widget_37)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zero_values_btn = QPushButton(self.widget_4)
        self.zero_values_btn.setObjectName(u"zero_values_btn")
        self.zero_values_btn.setMinimumSize(QSize(0, 40))
        self.zero_values_btn.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_2.addWidget(self.zero_values_btn)

        self.connect_tunel_btn = QPushButton(self.widget_4)
        self.connect_tunel_btn.setObjectName(u"connect_tunel_btn")
        self.connect_tunel_btn.setMinimumSize(QSize(0, 40))
        self.connect_tunel_btn.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_2.addWidget(self.connect_tunel_btn)

        self.disconnect_tunnel_btn = QPushButton(self.widget_4)
        self.disconnect_tunnel_btn.setObjectName(u"disconnect_tunnel_btn")
        self.disconnect_tunnel_btn.setMinimumSize(QSize(0, 40))
        self.disconnect_tunnel_btn.setMaximumSize(QSize(180, 40))

        self.horizontalLayout_2.addWidget(self.disconnect_tunnel_btn)

        self.widget_16 = QWidget(self.widget_4)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 44))
        self.widget_16.setMaximumSize(QSize(125, 16777215))
        self.widget_16.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_9 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stop_tunnel_btn = QPushButton(self.widget_16)
        self.stop_tunnel_btn.setObjectName(u"stop_tunnel_btn")
        self.stop_tunnel_btn.setEnabled(False)
        self.stop_tunnel_btn.setMaximumSize(QSize(124, 40))

        self.horizontalLayout_9.addWidget(self.stop_tunnel_btn)


        self.horizontalLayout_2.addWidget(self.widget_16)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.widget_9.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_19 = QWidget(self.widget_9)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_19)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_16)

        self.pump_chb = AnimatedToggle(self.widget_19)
        self.pump_chb.setObjectName(u"pump_chb")

        self.horizontalLayout_18.addWidget(self.pump_chb)

        self.label_17 = QLabel(self.widget_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_3.addWidget(self.widget_19)

        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.widget_18 = QWidget(self.widget_9)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_18)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_20.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.cooling_chb = AnimatedToggle(self.widget_18)
        self.cooling_chb.setObjectName(u"cooling_chb")

        self.horizontalLayout_20.addWidget(self.cooling_chb)

        self.label_20 = QLabel(self.widget_18)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_20.addWidget(self.label_20)


        self.horizontalLayout_3.addWidget(self.widget_18)


        self.verticalLayout.addWidget(self.widget_9)

        self.widget_40 = QWidget(self.widget)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(0, 35))
        self.widget_40.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.widget_20 = QWidget(self.widget_40)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_20)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(63, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.temp_lbl = QLabel(self.widget_20)
        self.temp_lbl.setObjectName(u"temp_lbl")
        self.temp_lbl.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_8.addWidget(self.temp_lbl)

        self.label_12 = QLabel(self.widget_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_8.addWidget(self.label_12)


        self.horizontalLayout.addWidget(self.widget_20)

        self.widget_5 = QWidget(self.widget_40)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.atm_pressure_lbl = QLabel(self.widget_5)
        self.atm_pressure_lbl.setObjectName(u"atm_pressure_lbl")

        self.horizontalLayout_10.addWidget(self.atm_pressure_lbl)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_40)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.humidity_lbl = QLabel(self.widget_7)
        self.humidity_lbl.setObjectName(u"humidity_lbl")

        self.horizontalLayout_11.addWidget(self.humidity_lbl)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)


        self.horizontalLayout.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_40)

        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_2 = QVBoxLayout(self.widget_11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_3)

        self.widget_13 = QWidget(self.widget_11)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.wind_velocity_lbl = QLabel(self.widget_13)
        self.wind_velocity_lbl.setObjectName(u"wind_velocity_lbl")
        self.wind_velocity_lbl.setMinimumSize(QSize(140, 0))
        self.wind_velocity_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.wind_velocity_lbl.setStyleSheet(u"")
        self.wind_velocity_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.wind_velocity_lbl)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout_5.addWidget(self.widget_14)

        self.label_7 = QLabel(self.widget_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.max_min_velocity_lbl = QLabel(self.widget_13)
        self.max_min_velocity_lbl.setObjectName(u"max_min_velocity_lbl")
        self.max_min_velocity_lbl.setMinimumSize(QSize(140, 0))
        self.max_min_velocity_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.max_min_velocity_lbl)


        self.verticalLayout_2.addWidget(self.widget_13)


        self.verticalLayout.addWidget(self.widget_11)

        self.widget_22 = QWidget(self.widget)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_6 = QVBoxLayout(self.widget_22)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(self.widget_22)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.label_13)

        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_23)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_14)

        self.average_temp_lbl = QLabel(self.widget_23)
        self.average_temp_lbl.setObjectName(u"average_temp_lbl")
        self.average_temp_lbl.setMinimumSize(QSize(140, 0))
        self.average_temp_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.average_temp_lbl.setStyleSheet(u"")
        self.average_temp_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.average_temp_lbl)

        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")

        self.horizontalLayout_13.addWidget(self.widget_24)

        self.label_21 = QLabel(self.widget_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.max_min_temp_lbl = QLabel(self.widget_23)
        self.max_min_temp_lbl.setObjectName(u"max_min_temp_lbl")
        self.max_min_temp_lbl.setMinimumSize(QSize(140, 0))
        self.max_min_temp_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.max_min_temp_lbl)


        self.verticalLayout_6.addWidget(self.widget_23)


        self.verticalLayout.addWidget(self.widget_22)

        self.widget_15 = QWidget(self.widget)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_5 = QVBoxLayout(self.widget_15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.widget_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.label_8)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.pressure_lbl = QLabel(self.widget_17)
        self.pressure_lbl.setObjectName(u"pressure_lbl")
        self.pressure_lbl.setMinimumSize(QSize(140, 0))
        self.pressure_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.pressure_lbl.setStyleSheet(u"")
        self.pressure_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.pressure_lbl)

        self.widget_21 = QWidget(self.widget_17)
        self.widget_21.setObjectName(u"widget_21")

        self.horizontalLayout_7.addWidget(self.widget_21)

        self.label_11 = QLabel(self.widget_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.max_min_pressure_lbl = QLabel(self.widget_17)
        self.max_min_pressure_lbl.setObjectName(u"max_min_pressure_lbl")
        self.max_min_pressure_lbl.setMinimumSize(QSize(140, 0))
        self.max_min_pressure_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.max_min_pressure_lbl)


        self.verticalLayout_5.addWidget(self.widget_17)


        self.verticalLayout.addWidget(self.widget_15)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label_22 = QLabel(self.widget_12)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_3.addWidget(self.label_22)

        self.widget_3 = QWidget(self.widget_12)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_23 = QLabel(self.widget_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(100, 16777215))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_23)

        self.frequency_lbl = QLabel(self.widget_3)
        self.frequency_lbl.setObjectName(u"frequency_lbl")
        self.frequency_lbl.setMinimumSize(QSize(100, 40))
        self.frequency_lbl.setMaximumSize(QSize(40, 16777215))
        self.frequency_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frequency_lbl)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_12)

        self.widget_33 = QWidget(self.widget)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.widget_33)


        self.verticalLayout_4.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plc_not_connected_lbl.setText(QCoreApplication.translate("Form", u"Wind tunnel not connected", None))
        self.reserved_error_lbl.setText(QCoreApplication.translate("Form", u"Pressure device not connected", None))
        self.zero_values_btn.setText(QCoreApplication.translate("Form", u"Zero values", None))
        self.connect_tunel_btn.setText(QCoreApplication.translate("Form", u"Connect tunnel", None))
        self.disconnect_tunnel_btn.setText(QCoreApplication.translate("Form", u"Disconnect tunnel", None))
        self.stop_tunnel_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Pump:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"off", None))
        self.pump_chb.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"on", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Cooling:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"off", None))
        self.cooling_chb.setText("")
        self.label_20.setText(QCoreApplication.translate("Form", u"on", None))
        self.label.setText(QCoreApplication.translate("Form", u"Temp :", None))
        self.temp_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"A. pressure:", None))
        self.atm_pressure_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"hPa", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Humidity:", None))
        self.humidity_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"%", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Velocity (m/s)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Average:", None))
        self.wind_velocity_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Max-Min:", None))
        self.max_min_velocity_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Temperature (\u00b0C)", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Average:", None))
        self.average_temp_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Max-Min:", None))
        self.max_min_temp_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Pressure (Pa)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Average:", None))
        self.pressure_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Max-Mint:", None))
        self.max_min_pressure_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Fan frequency (Hz)", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Average:", None))
        self.frequency_lbl.setText(QCoreApplication.translate("Form", u"Hz", None))
    # retranslateUi

