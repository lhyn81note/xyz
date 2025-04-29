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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(964, 722)
        Form.setStyleSheet(u"            QLineEdit {\n"
"                border: 2px solid #2196F3;\n"
"                border-radius: 5px;\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"            }\n"
"            QCheckBox{\n"
"                border: 2px solid #2196F3;\n"
"                border-radius: 5px;\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border-color: #64B5F6;\n"
"            }\n"
"            QPushButton {\n"
"                border: 2px solid #2196F3;\n"
"                border-radius: 5px;\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"				background-color: rgb(0, 85, 127);\n"
"				color: rgb(255, 255, 255);\n"
"            }")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, 5, 5)
        self.wgt_flow = QWidget(self.widget)
        self.wgt_flow.setObjectName(u"wgt_flow")

        self.horizontalLayout.addWidget(self.wgt_flow)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.cmb_flow = QComboBox(self.widget_3)
        self.cmb_flow.setObjectName(u"cmb_flow")

        self.verticalLayout_3.addWidget(self.cmb_flow)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout_3.addWidget(self.widget_4)

        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.btn_start = QPushButton(self.widget_2)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout_2.addWidget(self.btn_start)

        self.btb_stop = QPushButton(self.widget_2)
        self.btb_stop.setObjectName(u"btb_stop")
        self.btb_stop.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.btb_stop)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6d4b\u8bd5\u6d41\u7a0b", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6d41\u7a0b", None))
        self.btb_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u6d41\u7a0b", None))
    # retranslateUi

