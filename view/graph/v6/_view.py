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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.cmb_flow = QComboBox(self.widget_3)
        self.cmb_flow.setObjectName(u"cmb_flow")
        font1 = QFont()
        font1.setPointSize(11)
        self.cmb_flow.setFont(font1)

        self.verticalLayout_3.addWidget(self.cmb_flow)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_2)

        self.lb_flow_desc = QLabel(self.widget_5)
        self.lb_flow_desc.setObjectName(u"lb_flow_desc")
        self.lb_flow_desc.setFont(font1)

        self.verticalLayout_5.addWidget(self.lb_flow_desc)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_4)

        self.lb_flow_time = QLabel(self.widget_5)
        self.lb_flow_time.setObjectName(u"lb_flow_time")
        self.lb_flow_time.setFont(font1)

        self.verticalLayout_5.addWidget(self.lb_flow_time)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_3)

        self.pt_cmd_info = QPlainTextEdit(self.widget_6)
        self.pt_cmd_info.setObjectName(u"pt_cmd_info")

        self.verticalLayout_6.addWidget(self.pt_cmd_info)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)

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
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6d41\u7a0b\u63cf\u8ff0", None))
        self.lb_flow_desc.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65f6\u95f4", None))
        self.lb_flow_time.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6307\u4ee4\u4fe1\u606f", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6d41\u7a0b", None))
        self.btb_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u6d41\u7a0b", None))
    # retranslateUi

