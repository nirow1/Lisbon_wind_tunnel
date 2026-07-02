# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_pressure_viewXRAcgU.ui'
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
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.lbl_1_p_3 = QLabel(self.widget)
        self.lbl_1_p_3.setObjectName(u"lbl_1_p_3")

        self.gridLayout.addWidget(self.lbl_1_p_3, 0, 6, 1, 1)

        self.lbl_1_p_8 = QLabel(self.widget)
        self.lbl_1_p_8.setObjectName(u"lbl_1_p_8")

        self.gridLayout.addWidget(self.lbl_1_p_8, 0, 16, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 9, 1, 1)

        self.lbl_1_p_2 = QLabel(self.widget)
        self.lbl_1_p_2.setObjectName(u"lbl_1_p_2")

        self.gridLayout.addWidget(self.lbl_1_p_2, 0, 4, 1, 1)

        self.lbl_1_p_6 = QLabel(self.widget)
        self.lbl_1_p_6.setObjectName(u"lbl_1_p_6")

        self.gridLayout.addWidget(self.lbl_1_p_6, 0, 14, 1, 1)

        self.lbl_1_p_11 = QLabel(self.widget)
        self.lbl_1_p_11.setObjectName(u"lbl_1_p_11")

        self.gridLayout.addWidget(self.lbl_1_p_11, 1, 6, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_6, 0, 9, 1, 1)

        self.lbl_1_p_9 = QLabel(self.widget)
        self.lbl_1_p_9.setObjectName(u"lbl_1_p_9")

        self.gridLayout.addWidget(self.lbl_1_p_9, 1, 2, 1, 1)

        self.lbl_1_p_13 = QLabel(self.widget)
        self.lbl_1_p_13.setObjectName(u"lbl_1_p_13")

        self.gridLayout.addWidget(self.lbl_1_p_13, 1, 10, 1, 1)

        self.lbl_1_p_5 = QLabel(self.widget)
        self.lbl_1_p_5.setObjectName(u"lbl_1_p_5")

        self.gridLayout.addWidget(self.lbl_1_p_5, 0, 10, 1, 1)

        self.lbl_1_p_4 = QLabel(self.widget)
        self.lbl_1_p_4.setObjectName(u"lbl_1_p_4")

        self.gridLayout.addWidget(self.lbl_1_p_4, 0, 8, 1, 1)

        self.lbl_1_p_10 = QLabel(self.widget)
        self.lbl_1_p_10.setObjectName(u"lbl_1_p_10")

        self.gridLayout.addWidget(self.lbl_1_p_10, 0, 12, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_9, 0, 13, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 7, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 5, 1, 1)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 15, 1, 1)

        self.lbl_1_p_16 = QLabel(self.widget)
        self.lbl_1_p_16.setObjectName(u"lbl_1_p_16")

        self.gridLayout.addWidget(self.lbl_1_p_16, 1, 16, 1, 1)

        self.lbl_1_p_12 = QLabel(self.widget)
        self.lbl_1_p_12.setObjectName(u"lbl_1_p_12")

        self.gridLayout.addWidget(self.lbl_1_p_12, 1, 8, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 1, 13, 1, 1)

        self.lbl_1_p_14 = QLabel(self.widget)
        self.lbl_1_p_14.setObjectName(u"lbl_1_p_14")

        self.gridLayout.addWidget(self.lbl_1_p_14, 1, 12, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 1, 11, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_5, 0, 7, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_8, 0, 11, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.lbl_1_p_7 = QLabel(self.widget)
        self.lbl_1_p_7.setObjectName(u"lbl_1_p_7")

        self.gridLayout.addWidget(self.lbl_1_p_7, 1, 4, 1, 1)

        self.lbl_1_p_15 = QLabel(self.widget)
        self.lbl_1_p_15.setObjectName(u"lbl_1_p_15")

        self.gridLayout.addWidget(self.lbl_1_p_15, 1, 14, 1, 1)

        self.lbl_1_p_1 = QLabel(self.widget)
        self.lbl_1_p_1.setObjectName(u"lbl_1_p_1")

        self.gridLayout.addWidget(self.lbl_1_p_1, 0, 2, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 3, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_7, 0, 15, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_56 = QWidget(self.page)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(0, 35))
        self.widget_56.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(1, 1, 1, 1)
        self.label_2 = QLabel(self.widget_56)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_2)

        self.reset_pressure_chart_btn = QPushButton(self.widget_56)
        self.reset_pressure_chart_btn.setObjectName(u"reset_pressure_chart_btn")
        self.reset_pressure_chart_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_32.addWidget(self.reset_pressure_chart_btn)


        self.verticalLayout_3.addWidget(self.widget_56)

        self.widget_34 = QWidget(self.page)
        self.widget_34.setObjectName(u"widget_34")
        self.pressure_chart_lo = QHBoxLayout(self.widget_34)
        self.pressure_chart_lo.setObjectName(u"pressure_chart_lo")
        self.pressure_chart_lo.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_34)

        self.stackedWidget_3.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.widget_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.lbl_2_p_3 = QLabel(self.widget_5)
        self.lbl_2_p_3.setObjectName(u"lbl_2_p_3")

        self.gridLayout_2.addWidget(self.lbl_2_p_3, 0, 6, 1, 1)

        self.lbl_2_p_8 = QLabel(self.widget_5)
        self.lbl_2_p_8.setObjectName(u"lbl_2_p_8")

        self.gridLayout_2.addWidget(self.lbl_2_p_8, 0, 16, 1, 1)

        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 1, 9, 1, 1)

        self.lbl_2_p_2 = QLabel(self.widget_5)
        self.lbl_2_p_2.setObjectName(u"lbl_2_p_2")

        self.gridLayout_2.addWidget(self.lbl_2_p_2, 0, 4, 1, 1)

        self.lbl_2_p_7 = QLabel(self.widget_5)
        self.lbl_2_p_7.setObjectName(u"lbl_2_p_7")

        self.gridLayout_2.addWidget(self.lbl_2_p_7, 0, 14, 1, 1)

        self.lbl_2_p_11 = QLabel(self.widget_5)
        self.lbl_2_p_11.setObjectName(u"lbl_2_p_11")

        self.gridLayout_2.addWidget(self.lbl_2_p_11, 1, 6, 1, 1)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_15, 0, 9, 1, 1)

        self.lbl_2_p_9 = QLabel(self.widget_5)
        self.lbl_2_p_9.setObjectName(u"lbl_2_p_9")

        self.gridLayout_2.addWidget(self.lbl_2_p_9, 1, 2, 1, 1)

        self.lbl_2_p_13 = QLabel(self.widget_5)
        self.lbl_2_p_13.setObjectName(u"lbl_2_p_13")

        self.gridLayout_2.addWidget(self.lbl_2_p_13, 1, 10, 1, 1)

        self.lbl_2_p_5 = QLabel(self.widget_5)
        self.lbl_2_p_5.setObjectName(u"lbl_2_p_5")

        self.gridLayout_2.addWidget(self.lbl_2_p_5, 0, 10, 1, 1)

        self.lbl_2_p_4 = QLabel(self.widget_5)
        self.lbl_2_p_4.setObjectName(u"lbl_2_p_4")

        self.gridLayout_2.addWidget(self.lbl_2_p_4, 0, 8, 1, 1)

        self.lbl_2_p_6 = QLabel(self.widget_5)
        self.lbl_2_p_6.setObjectName(u"lbl_2_p_6")

        self.gridLayout_2.addWidget(self.lbl_2_p_6, 0, 12, 1, 1)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_16, 0, 13, 1, 1)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 7, 1, 1)

        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 1, 5, 1, 1)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 1, 15, 1, 1)

        self.lbl_2_p_16 = QLabel(self.widget_5)
        self.lbl_2_p_16.setObjectName(u"lbl_2_p_16")

        self.gridLayout_2.addWidget(self.lbl_2_p_16, 1, 16, 1, 1)

        self.lbl_2_p_12 = QLabel(self.widget_5)
        self.lbl_2_p_12.setObjectName(u"lbl_2_p_12")

        self.gridLayout_2.addWidget(self.lbl_2_p_12, 1, 8, 1, 1)

        self.label_28 = QLabel(self.widget_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 1, 13, 1, 1)

        self.lbl_2_p_14 = QLabel(self.widget_5)
        self.lbl_2_p_14.setObjectName(u"lbl_2_p_14")

        self.gridLayout_2.addWidget(self.lbl_2_p_14, 1, 12, 1, 1)

        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 1, 11, 1, 1)

        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_24, 0, 7, 1, 1)

        self.label_29 = QLabel(self.widget_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_29, 0, 11, 1, 1)

        self.label_30 = QLabel(self.widget_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_30, 0, 3, 1, 1)

        self.lbl_2_p_10 = QLabel(self.widget_5)
        self.lbl_2_p_10.setObjectName(u"lbl_2_p_10")

        self.gridLayout_2.addWidget(self.lbl_2_p_10, 1, 4, 1, 1)

        self.lbl_2_p_15 = QLabel(self.widget_5)
        self.lbl_2_p_15.setObjectName(u"lbl_2_p_15")

        self.gridLayout_2.addWidget(self.lbl_2_p_15, 1, 14, 1, 1)

        self.lbl_2_p_1 = QLabel(self.widget_5)
        self.lbl_2_p_1.setObjectName(u"lbl_2_p_1")

        self.gridLayout_2.addWidget(self.lbl_2_p_1, 0, 2, 1, 1)

        self.label_31 = QLabel(self.widget_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 1, 3, 1, 1)

        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_32, 0, 15, 1, 1)

        self.label_33 = QLabel(self.widget_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_33, 0, 5, 1, 1)

        self.label_34 = QLabel(self.widget_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.label_34, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_57 = QWidget(self.page_2)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(0, 35))
        self.widget_57.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(1, 1, 1, 1)
        self.label_14 = QLabel(self.widget_57)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_14)

        self.reset_pressure_chart_btn_2 = QPushButton(self.widget_57)
        self.reset_pressure_chart_btn_2.setObjectName(u"reset_pressure_chart_btn_2")
        self.reset_pressure_chart_btn_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_33.addWidget(self.reset_pressure_chart_btn_2)


        self.verticalLayout_2.addWidget(self.widget_57)

        self.widget_35 = QWidget(self.page_2)
        self.widget_35.setObjectName(u"widget_35")
        self.pressure_chart_lo_2 = QHBoxLayout(self.widget_35)
        self.pressure_chart_lo_2.setObjectName(u"pressure_chart_lo_2")
        self.pressure_chart_lo_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.widget_35)

        self.stackedWidget_3.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget_3)


        self.retranslateUi(Form)

        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.page_1_btn.setText(QCoreApplication.translate("Form", u"Page 1", None))
        self.page_2_btn.setText(QCoreApplication.translate("Form", u"Page 2", None))
        self.lbl_1_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"P13:", None))
        self.lbl_1_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"P5:", None))
        self.lbl_1_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_13.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"P7:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"P12:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"P11:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"P16:", None))
        self.lbl_1_p_16.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"P15:", None))
        self.lbl_1_p_14.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"P1:", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"P14:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"P4:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"P6:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"P2:", None))
        self.lbl_1_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_15.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_1_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"P10:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"P8:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"P3:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"P9:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pressures 1", None))
        self.reset_pressure_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart", None))
        self.lbl_2_p_3.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_8.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"P13:", None))
        self.lbl_2_p_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_7.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_11.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"P5:", None))
        self.lbl_2_p_9.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_13.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_5.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_4.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_6.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"P7:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"P12:", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"P11:", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"P16:", None))
        self.lbl_2_p_16.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_12.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"P15:", None))
        self.lbl_2_p_14.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"P1:", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"P14:", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"P4:", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"P6:", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"P2:", None))
        self.lbl_2_p_10.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_15.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.lbl_2_p_1.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"P10:", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"P8:", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"P3:", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"P9:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Pressures 2", None))
        self.reset_pressure_chart_btn_2.setText(QCoreApplication.translate("Form", u"Reset chart", None))
    # retranslateUi

