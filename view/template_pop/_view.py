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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(894, 595)
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
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_quest = QLineEdit(self.widget_2)
        self.tb_quest.setObjectName(u"tb_quest")

        self.horizontalLayout.addWidget(self.tb_quest)

        self.ck_manual = QCheckBox(self.widget_2)
        self.ck_manual.setObjectName(u"ck_manual")

        self.horizontalLayout.addWidget(self.ck_manual)

        self.btn_ask = QPushButton(self.widget_2)
        self.btn_ask.setObjectName(u"btn_ask")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ask.sizePolicy().hasHeightForWidth())
        self.btn_ask.setSizePolicy(sizePolicy)
        self.btn_ask.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.btn_ask)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tb_answer = QTextBrowser(self.widget)
        self.tb_answer.setObjectName(u"tb_answer")

        self.verticalLayout_2.addWidget(self.tb_answer)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ck_manual.setText(QCoreApplication.translate("Form", u"\u77e5\u8bc6\u5e93", None))
        self.btn_ask.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
    # retranslateUi

