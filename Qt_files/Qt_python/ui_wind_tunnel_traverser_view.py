# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_traverser_viewvsgSSy.ui'
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
        Form.resize(1357, 884)
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
"#widget_200, #widget_201, #widget_202, #widget_203, #widget_204, #widget_205, #widget_206, #widget_207, #widget_208, #widget_209, #widget_210, #widget_211, #widget_212, #widget_213, #widget_214{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.widget_13 = QWidget(Form)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pg_2d_btn = QPushButton(self.widget_13)
        self.pg_2d_btn.setObjectName(u"pg_2d_btn")
        self.pg_2d_btn.setMinimumSize(QSize(100, 0))
        self.pg_2d_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.pg_2d_btn)

        self.pg_3d_btn = QPushButton(self.widget_13)
        self.pg_3d_btn.setObjectName(u"pg_3d_btn")
        self.pg_3d_btn.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.pg_3d_btn)


        self.verticalLayout_5.addWidget(self.widget_13)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.drivers_2d_pg = QWidget()
        self.drivers_2d_pg.setObjectName(u"drivers_2d_pg")
        self.horizontalLayout_7 = QHBoxLayout(self.drivers_2d_pg)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_2 = QWidget(self.drivers_2d_pg)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(410, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_3.addWidget(self.label_20)

        self.widget_15 = QWidget(self.widget)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(400, 400))
        self.widget_15.setMaximumSize(QSize(400, 400))
        self.field_2d_lo = QHBoxLayout(self.widget_15)
        self.field_2d_lo.setObjectName(u"field_2d_lo")
        self.field_2d_lo.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_3.addWidget(self.widget_15)

        self.widget_19 = QWidget(self.widget)
        self.widget_19.setObjectName(u"widget_19")

        self.verticalLayout_3.addWidget(self.widget_19)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_204 = QWidget(self.widget_2)
        self.widget_204.setObjectName(u"widget_204")
        self.test_plan_2d_lo = QVBoxLayout(self.widget_204)
        self.test_plan_2d_lo.setObjectName(u"test_plan_2d_lo")
        self.test_plan_2d_lo.setContentsMargins(3, 3, 3, 3)
        self.connected_message_wg = QWidget(self.widget_204)
        self.connected_message_wg.setObjectName(u"connected_message_wg")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connected_message_wg.sizePolicy().hasHeightForWidth())
        self.connected_message_wg.setSizePolicy(sizePolicy)
        self.connected_message_wg.setMinimumSize(QSize(0, 0))
        self.connected_message_wg.setStyleSheet(u"QLabel {\n"
"    background-color: #FF3636;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.connected_message_wg)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_2 = QLabel(self.connected_message_wg)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setMinimumSize(QSize(0, 25))
        self.lbl_2.setMaximumSize(QSize(16777215, 25))
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.lbl_2)


        self.test_plan_2d_lo.addWidget(self.connected_message_wg)

        self.widget_5 = QWidget(self.widget_204)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 145))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_206 = QWidget(self.widget_5)
        self.widget_206.setObjectName(u"widget_206")
        self.widget_206.setMinimumSize(QSize(0, 130))
        self.widget_206.setMaximumSize(QSize(250, 130))
        self.gridLayout = QGridLayout(self.widget_206)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_206)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pos_x_2d_lbl = QLabel(self.widget_206)
        self.pos_x_2d_lbl.setObjectName(u"pos_x_2d_lbl")

        self.gridLayout.addWidget(self.pos_x_2d_lbl, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_206)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget_206)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pos_y_2d_lbl = QLabel(self.widget_206)
        self.pos_y_2d_lbl.setObjectName(u"pos_y_2d_lbl")

        self.gridLayout.addWidget(self.pos_y_2d_lbl, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_206)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_206)

        self.widget_207 = QWidget(self.widget_5)
        self.widget_207.setObjectName(u"widget_207")
        self.widget_207.setMinimumSize(QSize(0, 13))
        self.widget_207.setMaximumSize(QSize(250, 130))
        self.gridLayout_2 = QGridLayout(self.widget_207)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.set_pos_x_2d_btn = QPushButton(self.widget_207)
        self.set_pos_x_2d_btn.setObjectName(u"set_pos_x_2d_btn")
        self.set_pos_x_2d_btn.setMinimumSize(QSize(35, 0))
        self.set_pos_x_2d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.set_pos_x_2d_btn, 1, 3, 1, 1)

        self.set_pos_y_2d_le = QLineEdit(self.widget_207)
        self.set_pos_y_2d_le.setObjectName(u"set_pos_y_2d_le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.set_pos_y_2d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_y_2d_le.setSizePolicy(sizePolicy1)
        self.set_pos_y_2d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.set_pos_y_2d_le, 2, 1, 1, 1)

        self.set_pos_y_2d_btn = QPushButton(self.widget_207)
        self.set_pos_y_2d_btn.setObjectName(u"set_pos_y_2d_btn")
        self.set_pos_y_2d_btn.setMinimumSize(QSize(50, 0))
        self.set_pos_y_2d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.set_pos_y_2d_btn, 2, 3, 1, 1)

        self.set_pos_x_2d_le = QLineEdit(self.widget_207)
        self.set_pos_x_2d_le.setObjectName(u"set_pos_x_2d_le")
        sizePolicy1.setHeightForWidth(self.set_pos_x_2d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_x_2d_le.setSizePolicy(sizePolicy1)
        self.set_pos_x_2d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.set_pos_x_2d_le, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_207)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget_207)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_207)

        self.widget_18 = QWidget(self.widget_5)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 44))
        self.widget_18.setMaximumSize(QSize(125, 16777215))
        self.widget_18.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_11 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stop_driver_2d_btn = QPushButton(self.widget_18)
        self.stop_driver_2d_btn.setObjectName(u"stop_driver_2d_btn")
        self.stop_driver_2d_btn.setEnabled(False)
        self.stop_driver_2d_btn.setMaximumSize(QSize(124, 40))

        self.horizontalLayout_11.addWidget(self.stop_driver_2d_btn)


        self.horizontalLayout_3.addWidget(self.widget_18)


        self.test_plan_2d_lo.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.widget_204)


        self.horizontalLayout_7.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.drivers_2d_pg)
        self.drivers_3d_pg = QWidget()
        self.drivers_3d_pg.setObjectName(u"drivers_3d_pg")
        self.horizontalLayout_8 = QHBoxLayout(self.drivers_3d_pg)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_3 = QWidget(self.drivers_3d_pg)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_3)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(370, 0))
        self.widget_16.setMaximumSize(QSize(370, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.label_19 = QLabel(self.widget_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.label_19)

        self.widget_200 = QWidget(self.widget_16)
        self.widget_200.setObjectName(u"widget_200")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_200.sizePolicy().hasHeightForWidth())
        self.widget_200.setSizePolicy(sizePolicy2)
        self.widget_200.setMinimumSize(QSize(350, 350))
        self.widget_200.setMaximumSize(QSize(350, 350))
        self.field_3d_xy_lo = QHBoxLayout(self.widget_200)
        self.field_3d_xy_lo.setObjectName(u"field_3d_xy_lo")
        self.field_3d_xy_lo.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_6.addWidget(self.widget_200)

        self.label_17 = QLabel(self.widget_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.label_17)

        self.widget_201 = QWidget(self.widget_16)
        self.widget_201.setObjectName(u"widget_201")
        sizePolicy2.setHeightForWidth(self.widget_201.sizePolicy().hasHeightForWidth())
        self.widget_201.setSizePolicy(sizePolicy2)
        self.widget_201.setMinimumSize(QSize(350, 350))
        self.widget_201.setMaximumSize(QSize(350, 350))
        self.field_3d_xz_lo = QHBoxLayout(self.widget_201)
        self.field_3d_xz_lo.setObjectName(u"field_3d_xz_lo")
        self.field_3d_xz_lo.setContentsMargins(1, 1, 1, 1)

        self.verticalLayout_6.addWidget(self.widget_201)


        self.horizontalLayout.addWidget(self.widget_16)

        self.widget_205 = QWidget(self.widget_3)
        self.widget_205.setObjectName(u"widget_205")
        self.test_plan_3d_lo = QVBoxLayout(self.widget_205)
        self.test_plan_3d_lo.setObjectName(u"test_plan_3d_lo")
        self.test_plan_3d_lo.setContentsMargins(3, 3, 3, 3)
        self.connected_message_wg_2 = QWidget(self.widget_205)
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
        self.verticalLayout_12 = QVBoxLayout(self.connected_message_wg_2)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_3 = QLabel(self.connected_message_wg_2)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setMinimumSize(QSize(0, 25))
        self.lbl_3.setMaximumSize(QSize(16777215, 25))
        self.lbl_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_3)


        self.test_plan_3d_lo.addWidget(self.connected_message_wg_2)

        self.widget_20 = QWidget(self.widget_205)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 145))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_203 = QWidget(self.widget_20)
        self.widget_203.setObjectName(u"widget_203")
        self.widget_203.setMinimumSize(QSize(0, 130))
        self.widget_203.setMaximumSize(QSize(250, 130))
        self.gridLayout_3 = QGridLayout(self.widget_203)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.set_pos_y_3d_lbl = QLabel(self.widget_203)
        self.set_pos_y_3d_lbl.setObjectName(u"set_pos_y_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_y_3d_lbl, 1, 1, 1, 1)

        self.set_pos_x_3d_lbl = QLabel(self.widget_203)
        self.set_pos_x_3d_lbl.setObjectName(u"set_pos_x_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_x_3d_lbl, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_203)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_9 = QLabel(self.widget_203)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_203)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_203)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_16 = QLabel(self.widget_203)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.set_pos_z_3d_lbl = QLabel(self.widget_203)
        self.set_pos_z_3d_lbl.setObjectName(u"set_pos_z_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_z_3d_lbl, 2, 1, 1, 1)

        self.label_18 = QLabel(self.widget_203)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 2, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_203)

        self.widget_202 = QWidget(self.widget_20)
        self.widget_202.setObjectName(u"widget_202")
        self.widget_202.setMinimumSize(QSize(0, 130))
        self.widget_202.setMaximumSize(QSize(250, 130))
        self.gridLayout_4 = QGridLayout(self.widget_202)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.set_pos_x_3d_btn = QPushButton(self.widget_202)
        self.set_pos_x_3d_btn.setObjectName(u"set_pos_x_3d_btn")
        self.set_pos_x_3d_btn.setMinimumSize(QSize(35, 0))
        self.set_pos_x_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_x_3d_btn, 1, 3, 1, 1)

        self.set_pos_y_3d_btn = QPushButton(self.widget_202)
        self.set_pos_y_3d_btn.setObjectName(u"set_pos_y_3d_btn")
        self.set_pos_y_3d_btn.setMinimumSize(QSize(50, 0))
        self.set_pos_y_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_y_3d_btn, 2, 3, 1, 1)

        self.label_15 = QLabel(self.widget_202)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.set_pos_y_3d_le = QLineEdit(self.widget_202)
        self.set_pos_y_3d_le.setObjectName(u"set_pos_y_3d_le")
        sizePolicy1.setHeightForWidth(self.set_pos_y_3d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_y_3d_le.setSizePolicy(sizePolicy1)
        self.set_pos_y_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_y_3d_le, 2, 1, 1, 1)

        self.set_pos_x_3d_le = QLineEdit(self.widget_202)
        self.set_pos_x_3d_le.setObjectName(u"set_pos_x_3d_le")
        sizePolicy1.setHeightForWidth(self.set_pos_x_3d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_x_3d_le.setSizePolicy(sizePolicy1)
        self.set_pos_x_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_x_3d_le, 1, 1, 1, 1)

        self.label_14 = QLabel(self.widget_202)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.set_pos_z_3d_le = QLineEdit(self.widget_202)
        self.set_pos_z_3d_le.setObjectName(u"set_pos_z_3d_le")
        self.set_pos_z_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_z_3d_le, 3, 1, 1, 1)

        self.set_pos_z_3d_btn = QPushButton(self.widget_202)
        self.set_pos_z_3d_btn.setObjectName(u"set_pos_z_3d_btn")
        self.set_pos_z_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_z_3d_btn, 3, 3, 1, 1)

        self.label_13 = QLabel(self.widget_202)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_202)

        self.widget_17 = QWidget(self.widget_20)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 44))
        self.widget_17.setMaximumSize(QSize(125, 16777215))
        self.widget_17.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_10 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stop_driver_3d_btn = QPushButton(self.widget_17)
        self.stop_driver_3d_btn.setObjectName(u"stop_driver_3d_btn")
        self.stop_driver_3d_btn.setEnabled(False)
        self.stop_driver_3d_btn.setMaximumSize(QSize(124, 40))

        self.horizontalLayout_10.addWidget(self.stop_driver_3d_btn)


        self.horizontalLayout_6.addWidget(self.widget_17)


        self.test_plan_3d_lo.addWidget(self.widget_20)


        self.horizontalLayout.addWidget(self.widget_205)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.drivers_3d_pg)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(400, 200))
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 87))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.continue_btn = QPushButton(self.widget_6)
        self.continue_btn.setObjectName(u"continue_btn")
        self.continue_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_5.addWidget(self.continue_btn)


        self.verticalLayout.addWidget(self.widget_6)


        self.horizontalLayout_4.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pg_2d_btn.setText(QCoreApplication.translate("Form", u"2D view", None))
        self.pg_3d_btn.setText(QCoreApplication.translate("Form", u"3D view", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Position X Y:", None))
        self.lbl_2.setText(QCoreApplication.translate("Form", u"Driver 2d not connected", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.pos_x_2d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.pos_y_2d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"mm", None))
        self.set_pos_x_2d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_y_2d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_x_2d_le.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.stop_driver_2d_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Field X Y:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Field X Z:", None))
        self.lbl_3.setText(QCoreApplication.translate("Form", u"Driver 3d not connected", None))
        self.set_pos_y_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.set_pos_x_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Pos Z:", None))
        self.set_pos_z_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"mm", None))
        self.set_pos_x_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_y_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Pos Z:", None))
        self.set_pos_x_3d_le.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.set_pos_z_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.stop_driver_3d_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"You are about to set positions for traversers. ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Are you sure you want to continue? ", None))
        self.continue_btn.setText(QCoreApplication.translate("Form", u"Yes continue", None))
    # retranslateUi

