# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_config_viewJRFsSj.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Gui.Custom_widgets.toggle import AnimatedToggle

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
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 117))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 100))
        self.widget_8.setMaximumSize(QSize(16777215, 120))
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dir_path_line = QLineEdit(self.widget_9)
        self.dir_path_line.setObjectName(u"dir_path_line")
        self.dir_path_line.setMinimumSize(QSize(0, 30))
        self.dir_path_line.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.dir_path_line)

        self.change_dir_btn = QPushButton(self.widget_9)
        self.change_dir_btn.setObjectName(u"change_dir_btn")
        self.change_dir_btn.setMaximumSize(QSize(30, 30))
        self.change_dir_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.change_dir_btn)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.file_name_le = QLineEdit(self.widget_10)
        self.file_name_le.setObjectName(u"file_name_le")
        self.file_name_le.setEnabled(True)
        self.file_name_le.setMinimumSize(QSize(0, 30))
        self.file_name_le.setMaximumSize(QSize(200, 16777215))
        self.file_name_le.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.file_name_le)

        self.set_name_btn = QPushButton(self.widget_10)
        self.set_name_btn.setObjectName(u"set_name_btn")
        self.set_name_btn.setMinimumSize(QSize(115, 30))
        self.set_name_btn.setMaximumSize(QSize(115, 30))

        self.horizontalLayout_5.addWidget(self.set_name_btn)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")

        self.horizontalLayout_5.addWidget(self.widget_11)

        self.save_timer_le = QLineEdit(self.widget_10)
        self.save_timer_le.setObjectName(u"save_timer_le")
        self.save_timer_le.setMinimumSize(QSize(0, 30))
        self.save_timer_le.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.save_timer_le)

        self.save_timer_chb = AnimatedToggle(self.widget_10)
        self.save_timer_chb.setObjectName(u"save_timer_chb")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_timer_chb.sizePolicy().hasHeightForWidth())
        self.save_timer_chb.setSizePolicy(sizePolicy)
        self.save_timer_chb.setMinimumSize(QSize(60, 0))
        self.save_timer_chb.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.save_timer_chb)

        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_10)


        self.horizontalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_20 = QWidget(self.widget)
        self.widget_20.setObjectName(u"widget_20")

        self.horizontalLayout.addWidget(self.widget_20)

        self.set_frequency_rb = QRadioButton(self.widget)
        self.set_frequency_rb.setObjectName(u"set_frequency_rb")
        self.set_frequency_rb.setMinimumSize(QSize(200, 0))
        self.set_frequency_rb.setCheckable(True)

        self.horizontalLayout.addWidget(self.set_frequency_rb)

        self.set_frequency_le = QLineEdit(self.widget)
        self.set_frequency_le.setObjectName(u"set_frequency_le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.set_frequency_le.sizePolicy().hasHeightForWidth())
        self.set_frequency_le.setSizePolicy(sizePolicy1)
        self.set_frequency_le.setMaximumSize(QSize(200, 30))
        self.set_frequency_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.set_frequency_le)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout.addWidget(self.widget_12)

        self.set_velocity_rb = QRadioButton(self.widget)
        self.set_velocity_rb.setObjectName(u"set_velocity_rb")
        self.set_velocity_rb.setMinimumSize(QSize(200, 0))
        self.set_velocity_rb.setCheckable(True)

        self.horizontalLayout.addWidget(self.set_velocity_rb)

        self.set_velocity_le = QLineEdit(self.widget)
        self.set_velocity_le.setObjectName(u"set_velocity_le")
        sizePolicy1.setHeightForWidth(self.set_velocity_le.sizePolicy().hasHeightForWidth())
        self.set_velocity_le.setSizePolicy(sizePolicy1)
        self.set_velocity_le.setMaximumSize(QSize(200, 30))
        self.set_velocity_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.set_velocity_le)

        self.widget_16 = QWidget(self.widget)
        self.widget_16.setObjectName(u"widget_16")

        self.horizontalLayout.addWidget(self.widget_16)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_14 = QWidget(self.widget_2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.start_tunnel_btn = QPushButton(self.widget_14)
        self.start_tunnel_btn.setObjectName(u"start_tunnel_btn")
        self.start_tunnel_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_11.addWidget(self.start_tunnel_btn)

        self.widget_27 = QWidget(self.widget_14)
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


        self.verticalLayout_2.addWidget(self.widget_14)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.scale_chart = QVBoxLayout(self.widget_4)
        self.scale_chart.setObjectName(u"scale_chart")
        self.scale_chart.setContentsMargins(3, 3, 3, 3)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_2.addWidget(self.widget_6)

        self.restart_chart_btn = QPushButton(self.widget_5)
        self.restart_chart_btn.setObjectName(u"restart_chart_btn")
        self.restart_chart_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.restart_chart_btn)

        self.widget_13 = QWidget(self.widget_5)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777, 16777215))

        self.horizontalLayout_2.addWidget(self.widget_13)


        self.scale_chart.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.change_dir_btn.setText("")
        self.set_name_btn.setText(QCoreApplication.translate("Form", u"Set name", None))
        self.save_timer_chb.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Timer", None))
        self.set_frequency_rb.setText(QCoreApplication.translate("Form", u"Imposed frequency (Hz):", None))
        self.set_frequency_le.setInputMask("")
        self.set_frequency_le.setText("")
        self.set_frequency_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-100", None))
        self.set_velocity_rb.setText(QCoreApplication.translate("Form", u"Imposed velocity (m/s):", None))
        self.set_velocity_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-100", None))
        self.start_tunnel_btn.setText(QCoreApplication.translate("Form", u"On", None))
        self.stop_tunnel_btn.setText(QCoreApplication.translate("Form", u"Off", None))
        self.restart_chart_btn.setText(QCoreApplication.translate("Form", u"Reset chart axis", None))
    # retranslateUi

