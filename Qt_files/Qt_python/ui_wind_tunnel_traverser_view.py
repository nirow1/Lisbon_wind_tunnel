# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_tunnel_traverser_viewrgPcLC.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(862, 477)
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
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 60))
        self.gridLayout = QGridLayout(self.widget_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pos_x_2d_lbl = QLabel(self.widget_9)
        self.pos_x_2d_lbl.setObjectName(u"pos_x_2d_lbl")

        self.gridLayout.addWidget(self.pos_x_2d_lbl, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pos_y_2d_lbl = QLabel(self.widget_9)
        self.pos_y_2d_lbl.setObjectName(u"pos_y_2d_lbl")

        self.gridLayout.addWidget(self.pos_y_2d_lbl, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.set_pos_x_2d_le = QLineEdit(self.widget_4)
        self.set_pos_x_2d_le.setObjectName(u"set_pos_x_2d_le")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_pos_x_2d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_x_2d_le.setSizePolicy(sizePolicy)
        self.set_pos_x_2d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.set_pos_x_2d_le, 1, 1, 1, 1)

        self.set_pos_y_2d_le = QLineEdit(self.widget_4)
        self.set_pos_y_2d_le.setObjectName(u"set_pos_y_2d_le")
        sizePolicy.setHeightForWidth(self.set_pos_y_2d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_y_2d_le.setSizePolicy(sizePolicy)
        self.set_pos_y_2d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.set_pos_y_2d_le, 2, 1, 1, 1)

        self.set_pos_x_2d_btn = QPushButton(self.widget_4)
        self.set_pos_x_2d_btn.setObjectName(u"set_pos_x_2d_btn")
        self.set_pos_x_2d_btn.setMinimumSize(QSize(35, 0))
        self.set_pos_x_2d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.set_pos_x_2d_btn, 1, 3, 1, 1)

        self.set_pos_y_2d_btn = QPushButton(self.widget_4)
        self.set_pos_y_2d_btn.setObjectName(u"set_pos_y_2d_btn")
        self.set_pos_y_2d_btn.setMinimumSize(QSize(50, 0))
        self.set_pos_y_2d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.set_pos_y_2d_btn, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout = QVBoxLayout(self.widget_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.test_running_wg = QWidget(self.widget_6)
        self.test_running_wg.setObjectName(u"test_running_wg")
        self.test_running_wg.setMinimumSize(QSize(0, 25))
        self.test_running_wg.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.test_running_wg)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.test_running_wg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.test_running_wg)

        self.tableWidget = QTableWidget(self.widget_6)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.tableWidget)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.widget_7.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_row_btn = QPushButton(self.widget_7)
        self.add_row_btn.setObjectName(u"add_row_btn")
        self.add_row_btn.setMinimumSize(QSize(0, 0))
        self.add_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_3.addWidget(self.add_row_btn)

        self.start_test_plan_btn = QPushButton(self.widget_7)
        self.start_test_plan_btn.setObjectName(u"start_test_plan_btn")
        self.start_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.start_test_plan_btn)

        self.stop_test_plan_btn = QPushButton(self.widget_7)
        self.stop_test_plan_btn.setObjectName(u"stop_test_plan_btn")
        self.stop_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.stop_test_plan_btn)

        self.delete_row_btn = QPushButton(self.widget_7)
        self.delete_row_btn.setObjectName(u"delete_row_btn")
        self.delete_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_3.addWidget(self.delete_row_btn)


        self.verticalLayout.addWidget(self.widget_7)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 90))
        self.gridLayout_3 = QGridLayout(self.widget_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.set_pos_y_3d_lbl = QLabel(self.widget_11)
        self.set_pos_y_3d_lbl.setObjectName(u"set_pos_y_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_y_3d_lbl, 1, 1, 1, 1)

        self.set_pos_x_3d_lbl = QLabel(self.widget_11)
        self.set_pos_x_3d_lbl.setObjectName(u"set_pos_x_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_x_3d_lbl, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_9 = QLabel(self.widget_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_16 = QLabel(self.widget_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.set_pos_z_3d_lbl = QLabel(self.widget_11)
        self.set_pos_z_3d_lbl.setObjectName(u"set_pos_z_3d_lbl")

        self.gridLayout_3.addWidget(self.set_pos_z_3d_lbl, 2, 1, 1, 1)

        self.label_18 = QLabel(self.widget_11)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 2, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 120))
        self.gridLayout_4 = QGridLayout(self.widget_12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.set_pos_y_3d_btn = QPushButton(self.widget_12)
        self.set_pos_y_3d_btn.setObjectName(u"set_pos_y_3d_btn")
        self.set_pos_y_3d_btn.setMinimumSize(QSize(50, 0))
        self.set_pos_y_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_y_3d_btn, 2, 3, 1, 1)

        self.set_pos_x_3d_btn = QPushButton(self.widget_12)
        self.set_pos_x_3d_btn.setObjectName(u"set_pos_x_3d_btn")
        self.set_pos_x_3d_btn.setMinimumSize(QSize(35, 0))
        self.set_pos_x_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_x_3d_btn, 1, 3, 1, 1)

        self.set_pos_x_3d_le = QLineEdit(self.widget_12)
        self.set_pos_x_3d_le.setObjectName(u"set_pos_x_3d_le")
        sizePolicy.setHeightForWidth(self.set_pos_x_3d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_x_3d_le.setSizePolicy(sizePolicy)
        self.set_pos_x_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_x_3d_le, 1, 1, 1, 1)

        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_13 = QLabel(self.widget_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.set_pos_y_3d_le = QLineEdit(self.widget_12)
        self.set_pos_y_3d_le.setObjectName(u"set_pos_y_3d_le")
        sizePolicy.setHeightForWidth(self.set_pos_y_3d_le.sizePolicy().hasHeightForWidth())
        self.set_pos_y_3d_le.setSizePolicy(sizePolicy)
        self.set_pos_y_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_y_3d_le, 2, 1, 1, 1)

        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.set_pos_z_3d_le = QLineEdit(self.widget_12)
        self.set_pos_z_3d_le.setObjectName(u"set_pos_z_3d_le")
        self.set_pos_z_3d_le.setMaximumSize(QSize(60, 30))

        self.gridLayout_4.addWidget(self.set_pos_z_3d_le, 3, 1, 1, 1)

        self.set_pos_z_3d_btn = QPushButton(self.widget_12)
        self.set_pos_z_3d_btn.setObjectName(u"set_pos_z_3d_btn")
        self.set_pos_z_3d_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.set_pos_z_3d_btn, 3, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_12)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_2 = QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.test_running_wg_2 = QWidget(self.widget_8)
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


        self.verticalLayout_2.addWidget(self.test_running_wg_2)

        self.tableWidget_2 = QTableWidget(self.widget_8)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.tableWidget_2)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.widget_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_row_btn_2 = QPushButton(self.widget_10)
        self.add_row_btn_2.setObjectName(u"add_row_btn_2")
        self.add_row_btn_2.setMinimumSize(QSize(0, 0))
        self.add_row_btn_2.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.add_row_btn_2)

        self.start_test_plan_btn_2 = QPushButton(self.widget_10)
        self.start_test_plan_btn_2.setObjectName(u"start_test_plan_btn_2")
        self.start_test_plan_btn_2.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.start_test_plan_btn_2)

        self.stop_test_plan_btn_2 = QPushButton(self.widget_10)
        self.stop_test_plan_btn_2.setObjectName(u"stop_test_plan_btn_2")
        self.stop_test_plan_btn_2.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.stop_test_plan_btn_2)

        self.delete_row_btn_2 = QPushButton(self.widget_10)
        self.delete_row_btn_2.setObjectName(u"delete_row_btn_2")
        self.delete_row_btn_2.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.delete_row_btn_2)


        self.verticalLayout_2.addWidget(self.widget_10)


        self.horizontalLayout.addWidget(self.widget_8)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.pos_x_2d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.pos_y_2d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.set_pos_x_2d_le.setText("")
        self.set_pos_x_2d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_y_2d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"test running", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Sek", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Pos X", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Pos Y", None));
        self.add_row_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.start_test_plan_btn.setText(QCoreApplication.translate("Form", u"Start plan", None))
        self.stop_test_plan_btn.setText(QCoreApplication.translate("Form", u"End plan", None))
        self.delete_row_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.set_pos_y_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.set_pos_x_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"mm", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Pos Z:", None))
        self.set_pos_z_3d_lbl.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"mm", None))
        self.set_pos_y_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_x_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.set_pos_x_3d_le.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Pos Y:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Pos X:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Pos Z:", None))
        self.set_pos_z_3d_btn.setText(QCoreApplication.translate("Form", u"Set", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"test running", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Sek", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Pos X", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Pos Y", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Pos Z", None));
        self.add_row_btn_2.setText(QCoreApplication.translate("Form", u"+", None))
        self.start_test_plan_btn_2.setText(QCoreApplication.translate("Form", u"Start plan", None))
        self.stop_test_plan_btn_2.setText(QCoreApplication.translate("Form", u"End plan", None))
        self.delete_row_btn_2.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

