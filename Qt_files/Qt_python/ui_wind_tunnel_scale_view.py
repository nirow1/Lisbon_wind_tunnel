# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_scale_viewZWlabZ.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(839, 477)
        Form.setMaximumSize(QSize(16777215, 16777215))
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(Form)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, -1, 1, 1)
        self.stackedWidget = QStackedWidget(self.widget_13)
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

        self.widget_34 = QWidget(self.tlaskan_view_pg)
        self.widget_34.setObjectName(u"widget_34")
        self.tlaskan_chart = QHBoxLayout(self.widget_34)
        self.tlaskan_chart.setObjectName(u"tlaskan_chart")
        self.tlaskan_chart.setContentsMargins(0, 0, 0, 0)

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

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.widget_49 = QWidget(self.widget_13)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.gerlitz_logo_lbl = QLabel(self.widget_49)
        self.gerlitz_logo_lbl.setObjectName(u"gerlitz_logo_lbl")
        self.gerlitz_logo_lbl.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_33.addWidget(self.gerlitz_logo_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer)

        self.j4_logo_lbl = QLabel(self.widget_49)
        self.j4_logo_lbl.setObjectName(u"j4_logo_lbl")
        self.j4_logo_lbl.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_33.addWidget(self.j4_logo_lbl)


        self.verticalLayout_6.addWidget(self.widget_49)


        self.verticalLayout.addWidget(self.widget_13)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.reset_pressure_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart", None))
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
        self.gerlitz_logo_lbl.setText("")
        self.j4_logo_lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

