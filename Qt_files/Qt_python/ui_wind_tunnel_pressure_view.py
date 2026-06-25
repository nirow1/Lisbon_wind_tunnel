# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_pressure_viewPPvAwg.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1061, 810)
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
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.tlaskan_view_pg = QWidget()
        self.tlaskan_view_pg.setObjectName(u"tlaskan_view_pg")
        self.tlaskan_view_pg.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.tlaskan_view_pg)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, -1, 2, -1)
        self.widget_56 = QWidget(self.tlaskan_view_pg)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(0, 35))
        self.widget_56.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(1, 1, 1, 1)
        self.reset_pressure_chart_btn = QPushButton(self.widget_56)
        self.reset_pressure_chart_btn.setObjectName(u"reset_pressure_chart_btn")
        self.reset_pressure_chart_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_32.addWidget(self.reset_pressure_chart_btn)


        self.verticalLayout_7.addWidget(self.widget_56)

        self.widget = QWidget(self.tlaskan_view_pg)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lbl_1_p_1 = QLabel(self.widget)
        self.lbl_1_p_1.setObjectName(u"lbl_1_p_1")

        self.horizontalLayout.addWidget(self.lbl_1_p_1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lbl_1_p_2 = QLabel(self.widget)
        self.lbl_1_p_2.setObjectName(u"lbl_1_p_2")

        self.horizontalLayout.addWidget(self.lbl_1_p_2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lbl_1_p_3 = QLabel(self.widget)
        self.lbl_1_p_3.setObjectName(u"lbl_1_p_3")

        self.horizontalLayout.addWidget(self.lbl_1_p_3)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lbl_1_p_4 = QLabel(self.widget)
        self.lbl_1_p_4.setObjectName(u"lbl_1_p_4")

        self.horizontalLayout.addWidget(self.lbl_1_p_4)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.lbl_1_p_5 = QLabel(self.widget)
        self.lbl_1_p_5.setObjectName(u"lbl_1_p_5")

        self.horizontalLayout.addWidget(self.lbl_1_p_5)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.lbl_1_p_10 = QLabel(self.widget)
        self.lbl_1_p_10.setObjectName(u"lbl_1_p_10")

        self.horizontalLayout.addWidget(self.lbl_1_p_10)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.lbl_1_p_6 = QLabel(self.widget)
        self.lbl_1_p_6.setObjectName(u"lbl_1_p_6")

        self.horizontalLayout.addWidget(self.lbl_1_p_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.lbl_1_p_8 = QLabel(self.widget)
        self.lbl_1_p_8.setObjectName(u"lbl_1_p_8")

        self.horizontalLayout.addWidget(self.lbl_1_p_8)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.lbl_1_p_9 = QLabel(self.widget)
        self.lbl_1_p_9.setObjectName(u"lbl_1_p_9")

        self.horizontalLayout.addWidget(self.lbl_1_p_9)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.lbl_1_p_7 = QLabel(self.widget)
        self.lbl_1_p_7.setObjectName(u"lbl_1_p_7")

        self.horizontalLayout.addWidget(self.lbl_1_p_7)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.lbl_1_p_11 = QLabel(self.widget)
        self.lbl_1_p_11.setObjectName(u"lbl_1_p_11")

        self.horizontalLayout.addWidget(self.lbl_1_p_11)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.lbl_1_p_12 = QLabel(self.widget)
        self.lbl_1_p_12.setObjectName(u"lbl_1_p_12")

        self.horizontalLayout.addWidget(self.lbl_1_p_12)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.lbl_1_p_13 = QLabel(self.widget)
        self.lbl_1_p_13.setObjectName(u"lbl_1_p_13")

        self.horizontalLayout.addWidget(self.lbl_1_p_13)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout.addWidget(self.label_25)

        self.lbl_1_p_14 = QLabel(self.widget)
        self.lbl_1_p_14.setObjectName(u"lbl_1_p_14")

        self.horizontalLayout.addWidget(self.lbl_1_p_14)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout.addWidget(self.label_27)

        self.lbl_1_p_15 = QLabel(self.widget)
        self.lbl_1_p_15.setObjectName(u"lbl_1_p_15")

        self.horizontalLayout.addWidget(self.lbl_1_p_15)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout.addWidget(self.label_19)

        self.lbl_1_p_16 = QLabel(self.widget)
        self.lbl_1_p_16.setObjectName(u"lbl_1_p_16")

        self.horizontalLayout.addWidget(self.lbl_1_p_16)


        self.verticalLayout_7.addWidget(self.widget)

        self.widget_34 = QWidget(self.tlaskan_view_pg)
        self.widget_34.setObjectName(u"widget_34")
        self.pressure_chart_lo = QHBoxLayout(self.widget_34)
        self.pressure_chart_lo.setObjectName(u"pressure_chart_lo")
        self.pressure_chart_lo.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.widget_34)

        self.stackedWidget.addWidget(self.tlaskan_view_pg)
        self.scale_view_pg = QWidget()
        self.scale_view_pg.setObjectName(u"scale_view_pg")
        self.verticalLayout_12 = QVBoxLayout(self.scale_view_pg)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, -1, 2, -1)
        self.widget_45 = QWidget(self.scale_view_pg)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(0, 35))
        self.widget_45.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.label_16 = QLabel(self.widget_45)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(200, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_16)

        self.fx_lbl = QLabel(self.widget_45)
        self.fx_lbl.setObjectName(u"fx_lbl")
        self.fx_lbl.setMinimumSize(QSize(0, 0))
        self.fx_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.fx_lbl)

        self.label_18 = QLabel(self.widget_45)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(200, 16777215))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.fy_lbl = QLabel(self.widget_45)
        self.fy_lbl.setObjectName(u"fy_lbl")
        self.fy_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.fy_lbl)

        self.label_2 = QLabel(self.widget_45)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_2)

        self.fz_lbl = QLabel(self.widget_45)
        self.fz_lbl.setObjectName(u"fz_lbl")
        self.fz_lbl.setMinimumSize(QSize(0, 0))
        self.fz_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.fz_lbl)

        self.label_15 = QLabel(self.widget_45)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(200, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_15)

        self.mx_lbl = QLabel(self.widget_45)
        self.mx_lbl.setObjectName(u"mx_lbl")
        self.mx_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.mx_lbl)

        self.label_20 = QLabel(self.widget_45)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(200, 16777215))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_20)

        self.my_lbl = QLabel(self.widget_45)
        self.my_lbl.setObjectName(u"my_lbl")
        self.my_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.my_lbl)

        self.label_22 = QLabel(self.widget_45)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(200, 16777215))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_22)

        self.mz_lbl = QLabel(self.widget_45)
        self.mz_lbl.setObjectName(u"mz_lbl")
        self.mz_lbl.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.mz_lbl)

        self.reset_scale_chart_btn = QPushButton(self.widget_45)
        self.reset_scale_chart_btn.setObjectName(u"reset_scale_chart_btn")
        self.reset_scale_chart_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_21.addWidget(self.reset_scale_chart_btn)


        self.verticalLayout_12.addWidget(self.widget_45)

        self.widget_18 = QWidget(self.scale_view_pg)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.widget_38 = QWidget(self.widget_18)
        self.widget_38.setObjectName(u"widget_38")
        self.scale_chart = QGridLayout(self.widget_38)
        self.scale_chart.setObjectName(u"scale_chart")
        self.scale_chart.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_23.addWidget(self.widget_38)


        self.verticalLayout_12.addWidget(self.widget_18)

        self.widget_50 = QWidget(self.scale_view_pg)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.widget_53 = QWidget(self.widget_50)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(1, 1, 1, 1)
        self.label_24 = QLabel(self.widget_53)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_24)

        self.currnet_x_lbl = QLabel(self.widget_53)
        self.currnet_x_lbl.setObjectName(u"currnet_x_lbl")

        self.horizontalLayout_29.addWidget(self.currnet_x_lbl)


        self.horizontalLayout_26.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.widget_50)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_30 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_54)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_26)

        self.currnet_y_lbl = QLabel(self.widget_54)
        self.currnet_y_lbl.setObjectName(u"currnet_y_lbl")

        self.horizontalLayout_30.addWidget(self.currnet_y_lbl)


        self.horizontalLayout_26.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.widget_50)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_55)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_28)

        self.currnet_z_lbl = QLabel(self.widget_55)
        self.currnet_z_lbl.setObjectName(u"currnet_z_lbl")

        self.horizontalLayout_31.addWidget(self.currnet_z_lbl)


        self.horizontalLayout_26.addWidget(self.widget_55)


        self.verticalLayout_12.addWidget(self.widget_50)

        self.widget_24 = QWidget(self.scale_view_pg)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.widget_24)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.label_14 = QLabel(self.widget_44)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(50, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_14)

        self.set_x_le = QLineEdit(self.widget_44)
        self.set_x_le.setObjectName(u"set_x_le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.set_x_le.sizePolicy().hasHeightForWidth())
        self.set_x_le.setSizePolicy(sizePolicy1)
        self.set_x_le.setMinimumSize(QSize(0, 0))
        self.set_x_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_20.addWidget(self.set_x_le)

        self.set_x_btn = QPushButton(self.widget_44)
        self.set_x_btn.setObjectName(u"set_x_btn")
        self.set_x_btn.setMinimumSize(QSize(0, 0))
        self.set_x_btn.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_20.addWidget(self.set_x_btn)


        self.horizontalLayout_17.addWidget(self.widget_44)

        self.widget_51 = QWidget(self.widget_24)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(1, 1, 1, 1)
        self.label_21 = QLabel(self.widget_51)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_21)

        self.set_y_le = QLineEdit(self.widget_51)
        self.set_y_le.setObjectName(u"set_y_le")
        sizePolicy1.setHeightForWidth(self.set_y_le.sizePolicy().hasHeightForWidth())
        self.set_y_le.setSizePolicy(sizePolicy1)
        self.set_y_le.setMinimumSize(QSize(0, 0))
        self.set_y_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_27.addWidget(self.set_y_le)

        self.set_y_btn = QPushButton(self.widget_51)
        self.set_y_btn.setObjectName(u"set_y_btn")
        self.set_y_btn.setMinimumSize(QSize(0, 0))
        self.set_y_btn.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_27.addWidget(self.set_y_btn)


        self.horizontalLayout_17.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_24)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(1, 1, 1, 1)
        self.label_23 = QLabel(self.widget_52)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(50, 16777215))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_23)

        self.set_z_le = QLineEdit(self.widget_52)
        self.set_z_le.setObjectName(u"set_z_le")
        sizePolicy1.setHeightForWidth(self.set_z_le.sizePolicy().hasHeightForWidth())
        self.set_z_le.setSizePolicy(sizePolicy1)
        self.set_z_le.setMinimumSize(QSize(0, 0))
        self.set_z_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_28.addWidget(self.set_z_le)

        self.set_z_btn = QPushButton(self.widget_52)
        self.set_z_btn.setObjectName(u"set_z_btn")
        self.set_z_btn.setMinimumSize(QSize(0, 0))
        self.set_z_btn.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_28.addWidget(self.set_z_btn)


        self.horizontalLayout_17.addWidget(self.widget_52)


        self.verticalLayout_12.addWidget(self.widget_24)

        self.stackedWidget.addWidget(self.scale_view_pg)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.stackedWidget_2 = QStackedWidget(Form)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.tlaskan_view_pg_2 = QWidget()
        self.tlaskan_view_pg_2.setObjectName(u"tlaskan_view_pg_2")
        self.tlaskan_view_pg_2.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.tlaskan_view_pg_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, -1, 2, -1)
        self.widget_57 = QWidget(self.tlaskan_view_pg_2)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(0, 35))
        self.widget_57.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(1, 1, 1, 1)
        self.reset_pressure_chart_btn_2 = QPushButton(self.widget_57)
        self.reset_pressure_chart_btn_2.setObjectName(u"reset_pressure_chart_btn_2")
        self.reset_pressure_chart_btn_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_33.addWidget(self.reset_pressure_chart_btn_2)


        self.verticalLayout_8.addWidget(self.widget_57)

        self.widget_2 = QWidget(self.tlaskan_view_pg_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.label_45 = QLabel(self.widget_2)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_2.addWidget(self.label_45)

        self.lbl_2_p_1 = QLabel(self.widget_2)
        self.lbl_2_p_1.setObjectName(u"lbl_2_p_1")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_1)

        self.label_47 = QLabel(self.widget_2)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_2.addWidget(self.label_47)

        self.lbl_2_p_2 = QLabel(self.widget_2)
        self.lbl_2_p_2.setObjectName(u"lbl_2_p_2")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_2)

        self.label_49 = QLabel(self.widget_2)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_2.addWidget(self.label_49)

        self.lbl_2_p_3 = QLabel(self.widget_2)
        self.lbl_2_p_3.setObjectName(u"lbl_2_p_3")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_3)

        self.label_51 = QLabel(self.widget_2)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_2.addWidget(self.label_51)

        self.lbl_2_p_4 = QLabel(self.widget_2)
        self.lbl_2_p_4.setObjectName(u"lbl_2_p_4")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_4)

        self.label_53 = QLabel(self.widget_2)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_2.addWidget(self.label_53)

        self.lbl_2_p_5 = QLabel(self.widget_2)
        self.lbl_2_p_5.setObjectName(u"lbl_2_p_5")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_5)

        self.label_55 = QLabel(self.widget_2)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_2.addWidget(self.label_55)

        self.lbl_2_p_6 = QLabel(self.widget_2)
        self.lbl_2_p_6.setObjectName(u"lbl_2_p_6")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_6)

        self.label_57 = QLabel(self.widget_2)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_2.addWidget(self.label_57)

        self.lbl_2_p_7 = QLabel(self.widget_2)
        self.lbl_2_p_7.setObjectName(u"lbl_2_p_7")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_7)

        self.label_59 = QLabel(self.widget_2)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_2.addWidget(self.label_59)

        self.lbl_2_p_8 = QLabel(self.widget_2)
        self.lbl_2_p_8.setObjectName(u"lbl_2_p_8")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_8)

        self.label_61 = QLabel(self.widget_2)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_2.addWidget(self.label_61)

        self.lbl_2_p_9 = QLabel(self.widget_2)
        self.lbl_2_p_9.setObjectName(u"lbl_2_p_9")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_9)

        self.label_63 = QLabel(self.widget_2)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_2.addWidget(self.label_63)

        self.lbl_2_p_10 = QLabel(self.widget_2)
        self.lbl_2_p_10.setObjectName(u"lbl_2_p_10")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_10)

        self.label_65 = QLabel(self.widget_2)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_2.addWidget(self.label_65)

        self.lbl_2_p_11 = QLabel(self.widget_2)
        self.lbl_2_p_11.setObjectName(u"lbl_2_p_11")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_11)

        self.label_67 = QLabel(self.widget_2)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_2.addWidget(self.label_67)

        self.lbl_2_p_12 = QLabel(self.widget_2)
        self.lbl_2_p_12.setObjectName(u"lbl_2_p_12")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_12)

        self.label_69 = QLabel(self.widget_2)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_2.addWidget(self.label_69)

        self.lbl_2_p_13 = QLabel(self.widget_2)
        self.lbl_2_p_13.setObjectName(u"lbl_2_p_13")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_13)

        self.label_71 = QLabel(self.widget_2)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_2.addWidget(self.label_71)

        self.lbl_2_p_14 = QLabel(self.widget_2)
        self.lbl_2_p_14.setObjectName(u"lbl_2_p_14")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_14)

        self.label_73 = QLabel(self.widget_2)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_2.addWidget(self.label_73)

        self.lbl_2_p_15 = QLabel(self.widget_2)
        self.lbl_2_p_15.setObjectName(u"lbl_2_p_15")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_15)

        self.label_75 = QLabel(self.widget_2)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_2.addWidget(self.label_75)

        self.lbl_2_p_16 = QLabel(self.widget_2)
        self.lbl_2_p_16.setObjectName(u"lbl_2_p_16")

        self.horizontalLayout_2.addWidget(self.lbl_2_p_16)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.widget_35 = QWidget(self.tlaskan_view_pg_2)
        self.widget_35.setObjectName(u"widget_35")
        self.pressure_chart_lo_2 = QHBoxLayout(self.widget_35)
        self.pressure_chart_lo_2.setObjectName(u"pressure_chart_lo_2")
        self.pressure_chart_lo_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.widget_35)

        self.stackedWidget_2.addWidget(self.tlaskan_view_pg_2)
        self.scale_view_pg_2 = QWidget()
        self.scale_view_pg_2.setObjectName(u"scale_view_pg_2")
        self.verticalLayout_13 = QVBoxLayout(self.scale_view_pg_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, -1, 2, -1)
        self.widget_46 = QWidget(self.scale_view_pg_2)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(0, 35))
        self.widget_46.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(1, 1, 1, 1)
        self.label_77 = QLabel(self.widget_46)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(200, 16777215))
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_77)

        self.fx_lbl_2 = QLabel(self.widget_46)
        self.fx_lbl_2.setObjectName(u"fx_lbl_2")
        self.fx_lbl_2.setMinimumSize(QSize(0, 0))
        self.fx_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.fx_lbl_2)

        self.label_78 = QLabel(self.widget_46)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(200, 16777215))
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_78)

        self.fy_lbl_2 = QLabel(self.widget_46)
        self.fy_lbl_2.setObjectName(u"fy_lbl_2")
        self.fy_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.fy_lbl_2)

        self.label_79 = QLabel(self.widget_46)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(200, 16777215))
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_79)

        self.fz_lbl_2 = QLabel(self.widget_46)
        self.fz_lbl_2.setObjectName(u"fz_lbl_2")
        self.fz_lbl_2.setMinimumSize(QSize(0, 0))
        self.fz_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.fz_lbl_2)

        self.label_80 = QLabel(self.widget_46)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(200, 16777215))
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_80)

        self.mx_lbl_2 = QLabel(self.widget_46)
        self.mx_lbl_2.setObjectName(u"mx_lbl_2")
        self.mx_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.mx_lbl_2)

        self.label_81 = QLabel(self.widget_46)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(200, 16777215))
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_81)

        self.my_lbl_2 = QLabel(self.widget_46)
        self.my_lbl_2.setObjectName(u"my_lbl_2")
        self.my_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.my_lbl_2)

        self.label_82 = QLabel(self.widget_46)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(200, 16777215))
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_82)

        self.mz_lbl_2 = QLabel(self.widget_46)
        self.mz_lbl_2.setObjectName(u"mz_lbl_2")
        self.mz_lbl_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_22.addWidget(self.mz_lbl_2)

        self.reset_scale_chart_btn_2 = QPushButton(self.widget_46)
        self.reset_scale_chart_btn_2.setObjectName(u"reset_scale_chart_btn_2")
        self.reset_scale_chart_btn_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_22.addWidget(self.reset_scale_chart_btn_2)


        self.verticalLayout_13.addWidget(self.widget_46)

        self.widget_19 = QWidget(self.scale_view_pg_2)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.horizontalLayout_24 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.widget_39 = QWidget(self.widget_19)
        self.widget_39.setObjectName(u"widget_39")
        self.scale_chart_2 = QGridLayout(self.widget_39)
        self.scale_chart_2.setObjectName(u"scale_chart_2")
        self.scale_chart_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_24.addWidget(self.widget_39)


        self.verticalLayout_13.addWidget(self.widget_19)

        self.widget_58 = QWidget(self.scale_view_pg_2)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(1, 1, 1, 1)
        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, 1, 1, 1)
        self.label_83 = QLabel(self.widget_59)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_83)

        self.currnet_x_lbl_2 = QLabel(self.widget_59)
        self.currnet_x_lbl_2.setObjectName(u"currnet_x_lbl_2")

        self.horizontalLayout_35.addWidget(self.currnet_x_lbl_2)


        self.horizontalLayout_34.addWidget(self.widget_59)

        self.widget_60 = QWidget(self.widget_58)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.widget_60)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_84)

        self.currnet_y_lbl_2 = QLabel(self.widget_60)
        self.currnet_y_lbl_2.setObjectName(u"currnet_y_lbl_2")

        self.horizontalLayout_36.addWidget(self.currnet_y_lbl_2)


        self.horizontalLayout_34.addWidget(self.widget_60)

        self.widget_61 = QWidget(self.widget_58)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.widget_61)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_85)

        self.currnet_z_lbl_2 = QLabel(self.widget_61)
        self.currnet_z_lbl_2.setObjectName(u"currnet_z_lbl_2")

        self.horizontalLayout_37.addWidget(self.currnet_z_lbl_2)


        self.horizontalLayout_34.addWidget(self.widget_61)


        self.verticalLayout_13.addWidget(self.widget_58)

        self.widget_25 = QWidget(self.scale_view_pg_2)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_47 = QWidget(self.widget_25)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(1, 1, 1, 1)
        self.label_86 = QLabel(self.widget_47)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(50, 16777215))
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_86)

        self.set_x_le_2 = QLineEdit(self.widget_47)
        self.set_x_le_2.setObjectName(u"set_x_le_2")
        sizePolicy1.setHeightForWidth(self.set_x_le_2.sizePolicy().hasHeightForWidth())
        self.set_x_le_2.setSizePolicy(sizePolicy1)
        self.set_x_le_2.setMinimumSize(QSize(0, 0))
        self.set_x_le_2.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_25.addWidget(self.set_x_le_2)

        self.set_x_btn_2 = QPushButton(self.widget_47)
        self.set_x_btn_2.setObjectName(u"set_x_btn_2")
        self.set_x_btn_2.setMinimumSize(QSize(0, 0))
        self.set_x_btn_2.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_25.addWidget(self.set_x_btn_2)


        self.horizontalLayout_18.addWidget(self.widget_47)

        self.widget_62 = QWidget(self.widget_25)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(1, 1, 1, 1)
        self.label_87 = QLabel(self.widget_62)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMaximumSize(QSize(50, 16777215))
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_87)

        self.set_y_le_2 = QLineEdit(self.widget_62)
        self.set_y_le_2.setObjectName(u"set_y_le_2")
        sizePolicy1.setHeightForWidth(self.set_y_le_2.sizePolicy().hasHeightForWidth())
        self.set_y_le_2.setSizePolicy(sizePolicy1)
        self.set_y_le_2.setMinimumSize(QSize(0, 0))
        self.set_y_le_2.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_38.addWidget(self.set_y_le_2)

        self.set_y_btn_2 = QPushButton(self.widget_62)
        self.set_y_btn_2.setObjectName(u"set_y_btn_2")
        self.set_y_btn_2.setMinimumSize(QSize(0, 0))
        self.set_y_btn_2.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_38.addWidget(self.set_y_btn_2)


        self.horizontalLayout_18.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_25)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(1, 1, 1, 1)
        self.label_88 = QLabel(self.widget_63)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(50, 16777215))
        self.label_88.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_88)

        self.set_z_le_2 = QLineEdit(self.widget_63)
        self.set_z_le_2.setObjectName(u"set_z_le_2")
        sizePolicy1.setHeightForWidth(self.set_z_le_2.sizePolicy().hasHeightForWidth())
        self.set_z_le_2.setSizePolicy(sizePolicy1)
        self.set_z_le_2.setMinimumSize(QSize(0, 0))
        self.set_z_le_2.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_39.addWidget(self.set_z_le_2)

        self.set_z_btn_2 = QPushButton(self.widget_63)
        self.set_z_btn_2.setObjectName(u"set_z_btn_2")
        self.set_z_btn_2.setMinimumSize(QSize(0, 0))
        self.set_z_btn_2.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_39.addWidget(self.set_z_btn_2)


        self.horizontalLayout_18.addWidget(self.widget_63)


        self.verticalLayout_13.addWidget(self.widget_25)

        self.stackedWidget_2.addWidget(self.scale_view_pg_2)

        self.verticalLayout.addWidget(self.stackedWidget_2)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.reset_pressure_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart", None))
        self.label.setText(QCoreApplication.translate("Form", u"P1", None))
        self.lbl_1_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"P2", None))
        self.lbl_1_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"P3", None))
        self.lbl_1_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"P4", None))
        self.lbl_1_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"P5", None))
        self.lbl_1_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"P6", None))
        self.lbl_1_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"P7", None))
        self.lbl_1_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"P8", None))
        self.lbl_1_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"P9", None))
        self.lbl_1_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"P10", None))
        self.lbl_1_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"P11", None))
        self.lbl_1_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"P12", None))
        self.lbl_1_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"P13", None))
        self.lbl_1_p_13.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"P14", None))
        self.lbl_1_p_14.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"P15", None))
        self.lbl_1_p_15.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"P16", None))
        self.lbl_1_p_16.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Fx:", None))
        self.fx_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Fy:", None))
        self.fy_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Fz:", None))
        self.fz_lbl.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Mx:", None))
        self.mx_lbl.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"My:", None))
        self.my_lbl.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Mz:", None))
        self.mz_lbl.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.reset_scale_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Current X:", None))
        self.currnet_x_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Current Y:", None))
        self.currnet_y_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Current Z:", None))
        self.currnet_z_lbl.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"X:", None))
        self.set_x_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.set_y_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Z:", None))
        self.set_z_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.reset_pressure_chart_btn_2.setText(QCoreApplication.translate("Form", u"Reset chart", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"P1", None))
        self.lbl_2_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"P2", None))
        self.lbl_2_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"P3", None))
        self.lbl_2_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"P4", None))
        self.lbl_2_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"P5", None))
        self.lbl_2_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"P6", None))
        self.lbl_2_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"P7", None))
        self.lbl_2_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"P8", None))
        self.lbl_2_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"P9", None))
        self.lbl_2_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"P10", None))
        self.lbl_2_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"P11", None))
        self.lbl_2_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"P12", None))
        self.lbl_2_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"P13", None))
        self.lbl_2_p_13.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"P14", None))
        self.lbl_2_p_14.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_73.setText(QCoreApplication.translate("Form", u"P15", None))
        self.lbl_2_p_15.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"P16", None))
        self.lbl_2_p_16.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"Fx:", None))
        self.fx_lbl_2.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"Fy:", None))
        self.fy_lbl_2.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"Fz:", None))
        self.fz_lbl_2.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"Mx:", None))
        self.mx_lbl_2.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_81.setText(QCoreApplication.translate("Form", u"My:", None))
        self.my_lbl_2.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.label_82.setText(QCoreApplication.translate("Form", u"Mz:", None))
        self.mz_lbl_2.setText(QCoreApplication.translate("Form", u"00.0", None))
        self.reset_scale_chart_btn_2.setText(QCoreApplication.translate("Form", u"Reset chart", None))
        self.label_83.setText(QCoreApplication.translate("Form", u"Current X:", None))
        self.currnet_x_lbl_2.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_84.setText(QCoreApplication.translate("Form", u"Current Y:", None))
        self.currnet_y_lbl_2.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"Current Z:", None))
        self.currnet_z_lbl_2.setText(QCoreApplication.translate("Form", u"0.00", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"X:", None))
        self.set_x_btn_2.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.set_y_btn_2.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"Z:", None))
        self.set_z_btn_2.setText(QCoreApplication.translate("Form", u"Set", None))
    # retranslateUi

