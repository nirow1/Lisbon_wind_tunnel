# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Configuration_viewYnTReU.ui'
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
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 152))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_frequency_le.sizePolicy().hasHeightForWidth())
        self.set_frequency_le.setSizePolicy(sizePolicy)
        self.set_frequency_le.setMaximumSize(QSize(200, 30))
        self.set_frequency_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.set_frequency_le)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout.addWidget(self.widget_12)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_19 = QWidget(self.widget_5)
        self.widget_19.setObjectName(u"widget_19")

        self.horizontalLayout_2.addWidget(self.widget_19)

        self.set_velocity_rb = QRadioButton(self.widget_5)
        self.set_velocity_rb.setObjectName(u"set_velocity_rb")
        self.set_velocity_rb.setMinimumSize(QSize(200, 0))
        self.set_velocity_rb.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.set_velocity_rb)

        self.set_velocity_le = QLineEdit(self.widget_5)
        self.set_velocity_le.setObjectName(u"set_velocity_le")
        sizePolicy.setHeightForWidth(self.set_velocity_le.sizePolicy().hasHeightForWidth())
        self.set_velocity_le.setSizePolicy(sizePolicy)
        self.set_velocity_le.setMaximumSize(QSize(200, 30))
        self.set_velocity_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.set_velocity_le)

        self.widget_16 = QWidget(self.widget_5)
        self.widget_16.setObjectName(u"widget_16")

        self.horizontalLayout_2.addWidget(self.widget_16)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 310))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 40))
        self.widget_7.setMaximumSize(QSize(16777215, 56))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ramp_chb = AnimatedToggle(self.widget_7)
        self.ramp_chb.setObjectName(u"ramp_chb")
        self.ramp_chb.setMinimumSize(QSize(0, 0))
        self.ramp_chb.setMaximumSize(QSize(70, 40))

        self.horizontalLayout_4.addWidget(self.ramp_chb)

        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_17 = QWidget(self.widget_4)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_6 = QWidget(self.widget_17)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(300, 150))
        self.widget_6.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_15 = QWidget(self.widget_6)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(150, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.ramp_up_le = QLineEdit(self.widget_15)
        self.ramp_up_le.setObjectName(u"ramp_up_le")
        sizePolicy.setHeightForWidth(self.ramp_up_le.sizePolicy().hasHeightForWidth())
        self.ramp_up_le.setSizePolicy(sizePolicy)
        self.ramp_up_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_14.addWidget(self.ramp_up_le)

        self.ramp_up_btn = QPushButton(self.widget_15)
        self.ramp_up_btn.setObjectName(u"ramp_up_btn")
        self.ramp_up_btn.setMinimumSize(QSize(35, 0))
        self.ramp_up_btn.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_14.addWidget(self.ramp_up_btn)


        self.verticalLayout_4.addWidget(self.widget_15)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.run_duration_le = QLineEdit(self.widget_13)
        self.run_duration_le.setObjectName(u"run_duration_le")
        sizePolicy.setHeightForWidth(self.run_duration_le.sizePolicy().hasHeightForWidth())
        self.run_duration_le.setSizePolicy(sizePolicy)
        self.run_duration_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_3.addWidget(self.run_duration_le)

        self.run_duration_btn = QPushButton(self.widget_13)
        self.run_duration_btn.setObjectName(u"run_duration_btn")
        self.run_duration_btn.setMinimumSize(QSize(35, 0))
        self.run_duration_btn.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_3.addWidget(self.run_duration_btn)


        self.verticalLayout_4.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_6)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(150, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.ramp_down_le = QLineEdit(self.widget_14)
        self.ramp_down_le.setObjectName(u"ramp_down_le")
        sizePolicy.setHeightForWidth(self.ramp_down_le.sizePolicy().hasHeightForWidth())
        self.ramp_down_le.setSizePolicy(sizePolicy)
        self.ramp_down_le.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_13.addWidget(self.ramp_down_le)

        self.ramp_down_btn = QPushButton(self.widget_14)
        self.ramp_down_btn.setObjectName(u"ramp_down_btn")
        self.ramp_down_btn.setMinimumSize(QSize(35, 0))
        self.ramp_down_btn.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_13.addWidget(self.ramp_down_btn)


        self.verticalLayout_4.addWidget(self.widget_14)


        self.horizontalLayout_7.addWidget(self.widget_6)

        self.ramp_img_lbl = QLabel(self.widget_17)
        self.ramp_img_lbl.setObjectName(u"ramp_img_lbl")
        self.ramp_img_lbl.setMinimumSize(QSize(0, 0))
        self.ramp_img_lbl.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_7.addWidget(self.ramp_img_lbl)


        self.verticalLayout_3.addWidget(self.widget_17)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 178))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 100))
        self.widget_8.setMaximumSize(QSize(16777215, 120))
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_timer_chb.sizePolicy().hasHeightForWidth())
        self.save_timer_chb.setSizePolicy(sizePolicy1)
        self.save_timer_chb.setMinimumSize(QSize(60, 0))
        self.save_timer_chb.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.save_timer_chb)

        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_10)


        self.horizontalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.set_frequency_rb.setText(QCoreApplication.translate("Form", u"Imposed frequency (Hz):", None))
        self.set_frequency_le.setInputMask("")
        self.set_frequency_le.setText("")
        self.set_frequency_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-100", None))
        self.set_velocity_rb.setText(QCoreApplication.translate("Form", u"Imposed velocity (m/s):", None))
        self.set_velocity_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-100", None))
        self.ramp_chb.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Run parametrisation", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Ramp up (s):", None))
        self.ramp_up_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-1000", None))
        self.ramp_up_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Run duration (s):", None))
        self.run_duration_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-1000", None))
        self.run_duration_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Ramp down (s):", None))
        self.ramp_down_le.setPlaceholderText(QCoreApplication.translate("Form", u"0-1000", None))
        self.ramp_down_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.ramp_img_lbl.setText(QCoreApplication.translate("Form", u"RAMP_IMG", None))
        self.change_dir_btn.setText("")
        self.set_name_btn.setText(QCoreApplication.translate("Form", u"Set name", None))
        self.save_timer_chb.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Timer", None))
    # retranslateUi

