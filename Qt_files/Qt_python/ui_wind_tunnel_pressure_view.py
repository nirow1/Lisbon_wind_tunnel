# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_pressure_viewBQCfLz.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1187, 810)
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
"#widget, {\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.page_1_btn = QPushButton(self.widget_3)
        self.page_1_btn.setObjectName(u"page_1_btn")
        self.page_1_btn.setMinimumSize(QSize(0, 0))
        self.page_1_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.page_1_btn)

        self.page_2_btn = QPushButton(self.widget_3)
        self.page_2_btn.setObjectName(u"page_2_btn")
        self.page_2_btn.setMinimumSize(QSize(0, 0))
        self.page_2_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.page_2_btn)


        self.verticalLayout.addWidget(self.widget_3)

        self.stackedWidget_3 = QStackedWidget(Form)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.connected_message_wg_1 = QWidget(self.page)
        self.connected_message_wg_1.setObjectName(u"connected_message_wg_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connected_message_wg_1.sizePolicy().hasHeightForWidth())
        self.connected_message_wg_1.setSizePolicy(sizePolicy)
        self.connected_message_wg_1.setMinimumSize(QSize(0, 0))
        self.connected_message_wg_1.setStyleSheet(u"QLabel {\n"
"    background-color: #FF3636;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.connected_message_wg_1)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lbl_4 = QLabel(self.connected_message_wg_1)
        self.lbl_4.setObjectName(u"lbl_4")
        self.lbl_4.setMinimumSize(QSize(0, 25))
        self.lbl_4.setMaximumSize(QSize(16777215, 25))
        self.lbl_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.lbl_4)


        self.verticalLayout_3.addWidget(self.connected_message_wg_1)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 11, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 15, 1, 1)

        self.lbl_1_p_11 = QLabel(self.widget)
        self.lbl_1_p_11.setObjectName(u"lbl_1_p_11")

        self.gridLayout.addWidget(self.lbl_1_p_11, 1, 14, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_10, 1, 9, 1, 1)

        self.lbl_1_p_7 = QLabel(self.widget)
        self.lbl_1_p_7.setObjectName(u"lbl_1_p_7")

        self.gridLayout.addWidget(self.lbl_1_p_7, 1, 6, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_7, 1, 7, 1, 1)

        self.lbl_1_p_9 = QLabel(self.widget)
        self.lbl_1_p_9.setObjectName(u"lbl_1_p_9")

        self.gridLayout.addWidget(self.lbl_1_p_9, 1, 10, 1, 1)

        self.lbl_1_p_10 = QLabel(self.widget)
        self.lbl_1_p_10.setObjectName(u"lbl_1_p_10")

        self.gridLayout.addWidget(self.lbl_1_p_10, 1, 12, 1, 1)

        self.lbl_1_p_12 = QLabel(self.widget)
        self.lbl_1_p_12.setObjectName(u"lbl_1_p_12")

        self.gridLayout.addWidget(self.lbl_1_p_12, 1, 16, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_8, 0, 15, 1, 1)

        self.lbl_1_p_1 = QLabel(self.widget)
        self.lbl_1_p_1.setObjectName(u"lbl_1_p_1")

        self.gridLayout.addWidget(self.lbl_1_p_1, 0, 6, 1, 1)

        self.lbl_1_p_2 = QLabel(self.widget)
        self.lbl_1_p_2.setObjectName(u"lbl_1_p_2")

        self.gridLayout.addWidget(self.lbl_1_p_2, 0, 8, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_6, 0, 13, 1, 1)

        self.lbl_1_p_3 = QLabel(self.widget)
        self.lbl_1_p_3.setObjectName(u"lbl_1_p_3")

        self.gridLayout.addWidget(self.lbl_1_p_3, 0, 10, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_9, 1, 5, 1, 1)

        self.lbl_1_p_6 = QLabel(self.widget)
        self.lbl_1_p_6.setObjectName(u"lbl_1_p_6")

        self.gridLayout.addWidget(self.lbl_1_p_6, 0, 16, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 13, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 9, 1, 1)

        self.lbl_1_p_5 = QLabel(self.widget)
        self.lbl_1_p_5.setObjectName(u"lbl_1_p_5")

        self.gridLayout.addWidget(self.lbl_1_p_5, 0, 14, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_5, 0, 11, 1, 1)

        self.lbl_1_p_8 = QLabel(self.widget)
        self.lbl_1_p_8.setObjectName(u"lbl_1_p_8")

        self.gridLayout.addWidget(self.lbl_1_p_8, 1, 8, 1, 1)

        self.lbl_1_p_4 = QLabel(self.widget)
        self.lbl_1_p_4.setObjectName(u"lbl_1_p_4")

        self.gridLayout.addWidget(self.lbl_1_p_4, 0, 12, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_56 = QWidget(self.page)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(0, 35))
        self.widget_56.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.widget_56)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.reset_pressure_chart_btn = QPushButton(self.widget_56)
        self.reset_pressure_chart_btn.setObjectName(u"reset_pressure_chart_btn")
        self.reset_pressure_chart_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.reset_pressure_chart_btn)


        self.verticalLayout_3.addWidget(self.widget_56)

        self.widget_34 = QWidget(self.page)
        self.widget_34.setObjectName(u"widget_34")
        self.pressure_chart_lo = QHBoxLayout(self.widget_34)
        self.pressure_chart_lo.setObjectName(u"pressure_chart_lo")
        self.pressure_chart_lo.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_34)

        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 40))
        self.widget_4.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tare_device_1_btn = QPushButton(self.widget_4)
        self.tare_device_1_btn.setObjectName(u"tare_device_1_btn")
        self.tare_device_1_btn.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_5.addWidget(self.tare_device_1_btn)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.stackedWidget_3.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.connected_message_wg_2 = QWidget(self.page_2)
        self.connected_message_wg_2.setObjectName(u"connected_message_wg_2")
        sizePolicy.setHeightForWidth(self.connected_message_wg_2.sizePolicy().hasHeightForWidth())
        self.connected_message_wg_2.setSizePolicy(sizePolicy)
        self.connected_message_wg_2.setMinimumSize(QSize(0, 0))
        self.connected_message_wg_2.setStyleSheet(u"QLabel {\n"
"    background-color: #FF3636;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.connected_message_wg_2)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_2 = QLabel(self.connected_message_wg_2)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setMinimumSize(QSize(0, 25))
        self.lbl_2.setMaximumSize(QSize(16777215, 25))
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.lbl_2)


        self.verticalLayout_2.addWidget(self.connected_message_wg_2)

        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.widget_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_15, 1, 13, 1, 1)

        self.lbl_2_p_10 = QLabel(self.widget_5)
        self.lbl_2_p_10.setObjectName(u"lbl_2_p_10")

        self.gridLayout_2.addWidget(self.lbl_2_p_10, 2, 12, 1, 1)

        self.lbl_2_p_7 = QLabel(self.widget_5)
        self.lbl_2_p_7.setObjectName(u"lbl_2_p_7")

        self.gridLayout_2.addWidget(self.lbl_2_p_7, 2, 6, 1, 1)

        self.lbl_2_p_9 = QLabel(self.widget_5)
        self.lbl_2_p_9.setObjectName(u"lbl_2_p_9")

        self.gridLayout_2.addWidget(self.lbl_2_p_9, 2, 10, 1, 1)

        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 2, 13, 1, 1)

        self.lbl_2_p_6 = QLabel(self.widget_5)
        self.lbl_2_p_6.setObjectName(u"lbl_2_p_6")

        self.gridLayout_2.addWidget(self.lbl_2_p_6, 1, 16, 1, 1)

        self.lbl_2_p_4 = QLabel(self.widget_5)
        self.lbl_2_p_4.setObjectName(u"lbl_2_p_4")

        self.gridLayout_2.addWidget(self.lbl_2_p_4, 1, 12, 1, 1)

        self.lbl_2_p_3 = QLabel(self.widget_5)
        self.lbl_2_p_3.setObjectName(u"lbl_2_p_3")

        self.gridLayout_2.addWidget(self.lbl_2_p_3, 1, 10, 1, 1)

        self.lbl_2_p_1 = QLabel(self.widget_5)
        self.lbl_2_p_1.setObjectName(u"lbl_2_p_1")

        self.gridLayout_2.addWidget(self.lbl_2_p_1, 1, 6, 1, 1)

        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_24, 1, 11, 1, 1)

        self.label_29 = QLabel(self.widget_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_29, 1, 15, 1, 1)

        self.lbl_2_p_11 = QLabel(self.widget_5)
        self.lbl_2_p_11.setObjectName(u"lbl_2_p_11")

        self.gridLayout_2.addWidget(self.lbl_2_p_11, 2, 14, 1, 1)

        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_32, 2, 7, 1, 1)

        self.label_33 = QLabel(self.widget_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_33, 1, 9, 1, 1)

        self.label_34 = QLabel(self.widget_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_34, 2, 9, 1, 1)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_16, 2, 5, 1, 1)

        self.label_31 = QLabel(self.widget_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 2, 11, 1, 1)

        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_23, 1, 5, 1, 1)

        self.lbl_2_p_5 = QLabel(self.widget_5)
        self.lbl_2_p_5.setObjectName(u"lbl_2_p_5")

        self.gridLayout_2.addWidget(self.lbl_2_p_5, 1, 14, 1, 1)

        self.lbl_2_p_8 = QLabel(self.widget_5)
        self.lbl_2_p_8.setObjectName(u"lbl_2_p_8")

        self.gridLayout_2.addWidget(self.lbl_2_p_8, 2, 8, 1, 1)

        self.lbl_2_p_2 = QLabel(self.widget_5)
        self.lbl_2_p_2.setObjectName(u"lbl_2_p_2")

        self.gridLayout_2.addWidget(self.lbl_2_p_2, 1, 8, 1, 1)

        self.lbl_2_p_12 = QLabel(self.widget_5)
        self.lbl_2_p_12.setObjectName(u"lbl_2_p_12")

        self.gridLayout_2.addWidget(self.lbl_2_p_12, 2, 16, 1, 1)

        self.label_30 = QLabel(self.widget_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_30, 1, 7, 1, 1)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 2, 15, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_57 = QWidget(self.page_2)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(0, 35))
        self.widget_57.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout = QHBoxLayout(self.widget_57)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.label_14 = QLabel(self.widget_57)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_14)

        self.reset_pressure_chart_btn_2 = QPushButton(self.widget_57)
        self.reset_pressure_chart_btn_2.setObjectName(u"reset_pressure_chart_btn_2")
        self.reset_pressure_chart_btn_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.reset_pressure_chart_btn_2)


        self.verticalLayout_2.addWidget(self.widget_57)

        self.widget_35 = QWidget(self.page_2)
        self.widget_35.setObjectName(u"widget_35")
        self.pressure_chart_lo_2 = QHBoxLayout(self.widget_35)
        self.pressure_chart_lo_2.setObjectName(u"pressure_chart_lo_2")
        self.pressure_chart_lo_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.widget_35)

        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tare_device_2_btn = QPushButton(self.widget_2)
        self.tare_device_2_btn.setObjectName(u"tare_device_2_btn")
        self.tare_device_2_btn.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.tare_device_2_btn)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.stackedWidget_3.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget_3)


        self.retranslateUi(Form)

        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.page_1_btn.setText(QCoreApplication.translate("Form", u"Device 1", None))
        self.page_2_btn.setText(QCoreApplication.translate("Form", u"Device 2", None))
        self.lbl_4.setText(QCoreApplication.translate("Form", u"Devise 1 not connected", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"P10:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"P12:", None))
        self.lbl_1_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"P1:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"P9:", None))
        self.lbl_1_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"P8:", None))
        self.lbl_1_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"P6:", None))
        self.lbl_1_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"P5:", None))
        self.lbl_1_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"P7:", None))
        self.lbl_1_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"P11:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"P2:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"P3:", None))
        self.lbl_1_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"P4:", None))
        self.lbl_1_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Device 1", None))
        self.reset_pressure_chart_btn.setText(QCoreApplication.translate("Form", u"Reset axis", None))
        self.tare_device_1_btn.setText(QCoreApplication.translate("Form", u"Tare", None))
        self.lbl_2.setText(QCoreApplication.translate("Form", u"Device 2 not connected", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"P5:", None))
        self.lbl_2_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"P11:", None))
        self.lbl_2_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"P4:", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"P6:", None))
        self.lbl_2_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"P8:", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"P3:", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"P9:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"P7:", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"P10:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"P1:", None))
        self.lbl_2_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"P2:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"P12:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Device 2", None))
        self.reset_pressure_chart_btn_2.setText(QCoreApplication.translate("Form", u"Reset axis", None))
        self.tare_device_2_btn.setText(QCoreApplication.translate("Form", u"Tare", None))
    # retranslateUi

