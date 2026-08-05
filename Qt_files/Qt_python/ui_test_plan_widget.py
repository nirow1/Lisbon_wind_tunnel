# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_plan_widgetbaKozu.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1054, 578)
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
"#widget_200, #widget_201, #widget_202, #widget_203, #widget_204, #tableWidget{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_205 = QWidget(Form)
        self.widget_205.setObjectName(u"widget_205")
        self.verticalLayout_3 = QVBoxLayout(self.widget_205)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_14 = QWidget(self.widget_205)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 3, 5, 3)
        self.label_9 = QLabel(self.widget_14)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.xml_file_dir_le = QLineEdit(self.widget_14)
        self.xml_file_dir_le.setObjectName(u"xml_file_dir_le")
        self.xml_file_dir_le.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_7.addWidget(self.xml_file_dir_le)

        self.xml_file_dir_btn = QPushButton(self.widget_14)
        self.xml_file_dir_btn.setObjectName(u"xml_file_dir_btn")
        self.xml_file_dir_btn.setMinimumSize(QSize(40, 35))
        self.xml_file_dir_btn.setIconSize(QSize(40, 35))

        self.horizontalLayout_7.addWidget(self.xml_file_dir_btn)


        self.verticalLayout_3.addWidget(self.widget_14)

        self.test_running_wg = QWidget(self.widget_205)
        self.test_running_wg.setObjectName(u"test_running_wg")
        self.test_running_wg.setMinimumSize(QSize(0, 25))
        self.test_running_wg.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 7px;\n"
"    color: white; /* Optional: makes the text readable on red */\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.test_running_wg)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.test_running_wg)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.test_running_wg)

        self.tableWidget = QTableWidget(self.widget_205)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.widget_10 = QWidget(self.widget_205)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.widget_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_3d_row_btn = QPushButton(self.widget_10)
        self.add_3d_row_btn.setObjectName(u"add_3d_row_btn")
        self.add_3d_row_btn.setMinimumSize(QSize(0, 0))
        self.add_3d_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.add_3d_row_btn)

        self.start_test_plan_btn = QPushButton(self.widget_10)
        self.start_test_plan_btn.setObjectName(u"start_test_plan_btn")
        self.start_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.start_test_plan_btn)

        self.stop_test_plan_btn = QPushButton(self.widget_10)
        self.stop_test_plan_btn.setObjectName(u"stop_test_plan_btn")
        self.stop_test_plan_btn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.stop_test_plan_btn)

        self.delete_3d_row_btn = QPushButton(self.widget_10)
        self.delete_3d_row_btn.setObjectName(u"delete_3d_row_btn")
        self.delete_3d_row_btn.setMaximumSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.delete_3d_row_btn)


        self.verticalLayout_3.addWidget(self.widget_10)


        self.verticalLayout.addWidget(self.widget_205)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Load plan:", None))
        self.xml_file_dir_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"test running", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Sek", None));
        self.add_3d_row_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.start_test_plan_btn.setText(QCoreApplication.translate("Form", u"Start plan", None))
        self.stop_test_plan_btn.setText(QCoreApplication.translate("Form", u"End plan", None))
        self.delete_3d_row_btn.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

