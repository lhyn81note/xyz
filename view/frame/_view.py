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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

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
        self.wgt_root.setStyleSheet(u"QWidget{\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    /* \u57fa\u7840\u6837\u5f0f */\n"
"    background-color: #4CAF50;  /* \u9ed8\u8ba4\u80cc\u666f\u8272\uff08\u7eff\u8272\uff09 */\n"
"    color: black;              /* \u6587\u5b57\u989c\u8272 */\n"
"    border: 1px solid transparent;              /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 8px;        /* \u5706\u89d2 */\n"
"    padding: 3px 5px;         /* \u5185\u8fb9\u8ddd */\n"
"    font-size: 12px;           /* \u5b57\u4f53\u5927\u5c0f */\n"
"     /* font-weight: bold;         \u52a0\u7c97 */\n"
"    text-align: center;        /* \u6587\u5b57\u5c45\u4e2d */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;  /* \u80cc\u666f\u8272\u53d8\u6df1 */\n"
"    border-color: #80BDFF;      /* \u60ac\u505c\u65f6\u663e\u793a\u84dd\u8272\u8fb9\u6846 */\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton:pressed {\n"
"    background-color: #111111;  /* \u80cc\u666f\u8272\u66f4\u6df1 */\n"
"    "
                        "border-color: #222222;      /* \u6309\u4e0b\u65f6\u663e\u793a\u6df1\u84dd\u8272\u8fb9\u6846 *//\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;  /* \u7070\u8272\u80cc\u666f */\n"
"    color: #888888;            /* \u7070\u8272\u6587\u5b57 */\n"
"    border-color: #dddddd;     /* \u7070\u8272\u8fb9\u6846 */\n"
"    cursor: not-allowed;       /* \u7981\u6b62\u5149\u6807 */\n"
"}\n"
"\n"
"/* \u805a\u7126\u72b6\u6001\uff08\u53ef\u9009\uff09 */\n"
"QPushButton:focus {\n"
"    outline: none;             /* \u79fb\u9664\u9ed8\u8ba4\u7126\u70b9\u8f6e\u5ed3 */\n"
"    border-color: #4d90fe;     /* \u805a\u7126\u65f6\u663e\u793a\u6df1\u84dd\u8272\u8fb9\u6846 */\n"
"}")
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
        self.logo = QLabel(self.wgt_head)
        self.logo.setObjectName(u"logo")
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.wgt_info = QWidget(self.wgt_head)
        self.wgt_info.setObjectName(u"wgt_info")
        self.wgt_info.setMinimumSize(QSize(0, 60))
        self.wgt_info.setMaximumSize(QSize(16777215, 60))
        self.wgt_info.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.wgt_info)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.wgt_info)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 26pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.wgt_info)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"padding-bottom: 0px;  /* \u5e95\u90e8\u5185\u8fb9\u8ddd\u8bbe\u4e3a0 */\n"
"padding-left: 0px;  /* \u5e95\u90e8\u5185\u8fb9\u8ddd\u8bbe\u4e3a0 */\n"
"margin-bottom: 0px;   /* \u5e95\u90e8\u5916\u8fb9\u8ddd\u8bbe\u4e3a0 */\n"
"height: 30px;  ")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.wgt_info)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addWidget(self.wgt_head)

        self.wgt_view = QWidget(self.wgt_root)
        self.wgt_view.setObjectName(u"wgt_view")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.wgt_view.setFont(font2)

        self.verticalLayout.addWidget(self.wgt_view)

        self.wgt_status = QWidget(self.wgt_root)
        self.wgt_status.setObjectName(u"wgt_status")
        self.wgt_status.setMinimumSize(QSize(0, 30))
        self.wgt_status.setMaximumSize(QSize(16777215, 30))
        self.wgt_status.setStyleSheet(u"QWidget{\n"
"background-color: rgb(204, 204, 204);\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-color: rgb(76, 76, 76);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.wgt_status)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.lb_status_plc = QLabel(self.wgt_status)
        self.lb_status_plc.setObjectName(u"lb_status_plc")
        self.lb_status_plc.setStyleSheet(u"background-color: rgb(236, 36, 39);")

        self.horizontalLayout_3.addWidget(self.lb_status_plc)

        self.lb_status_serial = QLabel(self.wgt_status)
        self.lb_status_serial.setObjectName(u"lb_status_serial")
        self.lb_status_serial.setStyleSheet(u"background-color: rgb(236, 36, 39);")

        self.horizontalLayout_3.addWidget(self.lb_status_serial)

        self.lb_status_other = QLabel(self.wgt_status)
        self.lb_status_other.setObjectName(u"lb_status_other")
        self.lb_status_other.setStyleSheet(u"background-color: rgb(236, 36, 39);")

        self.horizontalLayout_3.addWidget(self.lb_status_other)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lb_info = QLabel(self.wgt_status)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setStyleSheet(u"border-width:1px;\n"
"border-style:solid;\n"
"border-color: rgb(76, 76, 76);")

        self.horizontalLayout_3.addWidget(self.lb_info)

        self.pushButton_2 = QPushButton(self.wgt_status)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout.addWidget(self.wgt_status)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        MainWindow.setCentralWidget(self.wgt_root)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5411\u67b6\u9759\u8f7d\u8bd5\u9a8c\u53f0\u4e0a\u4f4d\u673a\u7a0b\u5e8f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u521b\u7248 V1.0", None))
        self.lb_status_plc.setText(QCoreApplication.translate("MainWindow", u"PLC", None))
        self.lb_status_serial.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u670d\u52a1\u5668", None))
        self.lb_status_other.setText(QCoreApplication.translate("MainWindow", u"XX\u4f20\u611f\u5668", None))
        self.lb_info.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7cfb\u7edf\u6d88\u606f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a\u6d88\u606f", None))
    # retranslateUi

