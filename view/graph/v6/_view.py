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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wgt_flow = QWidget(self.widget)
        self.wgt_flow.setObjectName(u"wgt_flow")

        self.verticalLayout_2.addWidget(self.wgt_flow)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6d41\u7a0b", None))
    # retranslateUi

