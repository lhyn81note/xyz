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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 595)
        Form.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 2px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetCenter = QWidget(Form)
        self.widgetCenter.setObjectName(u"widgetCenter")
        self.verticalLayout_2 = QVBoxLayout(self.widgetCenter)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widgetCenter)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.widget_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.widgetCenter)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonSave = QPushButton(self.widget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_3.addWidget(self.pushButtonSave)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButtonUpdate = QPushButton(self.widget)
        self.pushButtonUpdate.setObjectName(u"pushButtonUpdate")

        self.horizontalLayout_3.addWidget(self.pushButtonUpdate)

        self.pushButtonadd = QPushButton(self.widget)
        self.pushButtonadd.setObjectName(u"pushButtonadd")

        self.horizontalLayout_3.addWidget(self.pushButtonadd)

        self.pushButtondelete = QPushButton(self.widget)
        self.pushButtondelete.setObjectName(u"pushButtondelete")

        self.horizontalLayout_3.addWidget(self.pushButtondelete)

        self.pushButtoninsert = QPushButton(self.widget)
        self.pushButtoninsert.setObjectName(u"pushButtoninsert")

        self.horizontalLayout_3.addWidget(self.pushButtoninsert)

        self.pushButtonset = QPushButton(self.widget)
        self.pushButtonset.setObjectName(u"pushButtonset")

        self.horizontalLayout_3.addWidget(self.pushButtonset)

        self.pushButtonclear = QPushButton(self.widget)
        self.pushButtonclear.setObjectName(u"pushButtonclear")

        self.horizontalLayout_3.addWidget(self.pushButtonclear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widgetCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("Form", u"update", None))
        self.pushButtonadd.setText(QCoreApplication.translate("Form", u"add", None))
        self.pushButtondelete.setText(QCoreApplication.translate("Form", u"delete", None))
        self.pushButtoninsert.setText(QCoreApplication.translate("Form", u"insert", None))
        self.pushButtonset.setText(QCoreApplication.translate("Form", u"set", None))
        self.pushButtonclear.setText(QCoreApplication.translate("Form", u"clear", None))
    # retranslateUi

