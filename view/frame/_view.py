# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 783)
        MainWindow.setStyleSheet(u"QLabel{\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QPushButton{\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"border:none;\n"
"}")
        self.wgt_root = QWidget(MainWindow)
        self.wgt_root.setObjectName(u"wgt_root")
        self.verticalLayout = QVBoxLayout(self.wgt_root)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.wgt_head = QWidget(self.wgt_root)
        self.wgt_head.setObjectName(u"wgt_head")
        self.wgt_head.setMinimumSize(QSize(0, 80))
        self.wgt_head.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.wgt_head)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.wgt_info = QWidget(self.wgt_head)
        self.wgt_info.setObjectName(u"wgt_info")
        self.wgt_info.setMinimumSize(QSize(0, 60))
        self.wgt_info.setMaximumSize(QSize(16777215, 60))
        self.wgt_info.setStyleSheet(u"background-color: rgb(159, 159, 159);")
        self.horizontalLayout_2 = QHBoxLayout(self.wgt_info)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_alarm = QLabel(self.wgt_info)
        self.lb_alarm.setObjectName(u"lb_alarm")

        self.horizontalLayout_2.addWidget(self.lb_alarm)


        self.horizontalLayout.addWidget(self.wgt_info)

        self.logo = QLabel(self.wgt_head)
        self.logo.setObjectName(u"logo")
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.wgt_head)

        self.wgt_view = QWidget(self.wgt_root)
        self.wgt_view.setObjectName(u"wgt_view")

        self.verticalLayout.addWidget(self.wgt_view)

        self.wgt_status = QWidget(self.wgt_root)
        self.wgt_status.setObjectName(u"wgt_status")
        self.wgt_status.setMinimumSize(QSize(0, 30))
        self.wgt_status.setMaximumSize(QSize(16777215, 30))
        self.wgt_status.setStyleSheet(u"QWidget{\n"
"background-color: rgb(204, 204, 204);\n"
"}\n"
"QLabel{\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.wgt_status)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.widget = QWidget(self.wgt_status)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lb_plc = QLabel(self.widget)
        self.lb_plc.setObjectName(u"lb_plc")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.lb_plc.setFont(font)
        self.lb_plc.setStyleSheet(u"font: 20pt \"Agency FB\";\n"
"color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.lb_plc)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lb_info = QLabel(self.wgt_status)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setStyleSheet(u"border-width:1px;\n"
"border-style:solid;\n"
"border-color: rgb(76, 76, 76);")

        self.horizontalLayout_3.addWidget(self.lb_info)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.wgt_status)

        MainWindow.setCentralWidget(self.wgt_root)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_alarm.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u8b66\u4fe1\u606f", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PLC\u72b6\u6001", None))
        self.lb_plc.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.lb_info.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u6d88\u606f", None))
    # retranslateUi

