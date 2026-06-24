# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings_viewTjInFA.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(941, 751)
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
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 22):
            self.tableWidget.setRowCount(22)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout.addWidget(self.widget_2)

        self.set_changes_btn = QPushButton(self.widget)
        self.set_changes_btn.setObjectName(u"set_changes_btn")
        self.set_changes_btn.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.set_changes_btn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Current", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Requested", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Quantization noise clipping", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"PID Kp parameter", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"PID Ti parameter", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"PID Td parameter", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"D\u2011term filter coefficient", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"PID deadband", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Enable adaptive Kp for PID", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Adaptive Kp PID \u2013 low speed", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Adaptive Kp PID \u2013 value for low speed", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Adaptive Kp PID \u2013 high speed", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Adaptive Kp PID \u2013 value for high speed", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Enable D\u2011term calculation from Process Value", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Enable P\u2011term calculation from Process Value", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Enable Kalman filter from pressure", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Kalman R parameter", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Kalman Q parameter", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Enable Feed Forward", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Feed Forward for step change", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Upper speed tolerance for hold transition (SP + Tol) ", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Lower speed tolerance for hold transition (SP \u2013 Tol)", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Time the speed must remain within tolerance for hold transition", None));
        self.set_changes_btn.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

