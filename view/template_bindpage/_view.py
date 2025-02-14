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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QDoubleSpinBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableView, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_PageBogieModel(object):
    def setupUi(self, PageBogieModel):
        if not PageBogieModel.objectName():
            PageBogieModel.setObjectName(u"PageBogieModel")
        PageBogieModel.resize(925, 533)
        PageBogieModel.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout = QHBoxLayout(PageBogieModel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetCenter = QWidget(PageBogieModel)
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

        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 150))
        self.widget_3.setMaximumSize(QSize(16777215, 150))
        self.labelTest = QLabel(self.widget_3)
        self.labelTest.setObjectName(u"labelTest")
        self.labelTest.setGeometry(QRect(160, 50, 111, 31))
        self.labelTest.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 9pt \"Microsoft YaHei\";\n"
"border-color: rgb(255, 170, 255);")
        self.textEditAge = QTextEdit(self.widget_3)
        self.textEditAge.setObjectName(u"textEditAge")
        self.textEditAge.setGeometry(QRect(10, 50, 132, 32))
        self.textEditAge.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 170, 255);\n"
"font: 9pt \"Microsoft YaHei\";\n"
"border-color: rgb(255, 170, 255);")
        self.checkBoxTest = QCheckBox(self.widget_3)
        self.checkBoxTest.setObjectName(u"checkBoxTest")
        self.checkBoxTest.setGeometry(QRect(290, 60, 76, 18))
        self.checkBoxTest.setCheckable(True)
        self.checkBoxTest.setChecked(False)
        self.radioButtonTest1 = QRadioButton(self.widget_3)
        self.radioButtonTest1.setObjectName(u"radioButtonTest1")
        self.radioButtonTest1.setGeometry(QRect(390, 60, 90, 18))
        self.radioButtonTest1.setChecked(True)
        self.radioButtonTest2 = QRadioButton(self.widget_3)
        self.radioButtonTest2.setObjectName(u"radioButtonTest2")
        self.radioButtonTest2.setGeometry(QRect(490, 60, 90, 18))
        self.radioButtonTest2.setChecked(False)
        self.dateEdit = QDateEdit(self.widget_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(620, 20, 88, 20))
        self.timeEdit = QTimeEdit(self.widget_3)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(720, 20, 101, 20))
        self.dateTimeEdit = QDateTimeEdit(self.widget_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(620, 50, 171, 22))
        self.labelDateTimeTest = QLabel(self.widget_3)
        self.labelDateTimeTest.setObjectName(u"labelDateTimeTest")
        self.labelDateTimeTest.setGeometry(QRect(50, 10, 231, 16))
        self.labelDateTest = QLabel(self.widget_3)
        self.labelDateTest.setObjectName(u"labelDateTest")
        self.labelDateTest.setGeometry(QRect(280, 10, 101, 16))
        self.labelTimeTest = QLabel(self.widget_3)
        self.labelTimeTest.setObjectName(u"labelTimeTest")
        self.labelTimeTest.setGeometry(QRect(400, 10, 101, 16))
        self.comboBoxTest = QComboBox(self.widget_3)
        self.comboBoxTest.setObjectName(u"comboBoxTest")
        self.comboBoxTest.setGeometry(QRect(510, 10, 91, 22))
        self.pushButtonTest = QPushButton(self.widget_3)
        self.pushButtonTest.setObjectName(u"pushButtonTest")
        self.pushButtonTest.setGeometry(QRect(20, 110, 111, 31))
        self.plainTextEditTest = QPlainTextEdit(self.widget_3)
        self.plainTextEditTest.setObjectName(u"plainTextEditTest")
        self.plainTextEditTest.setGeometry(QRect(210, 110, 104, 41))
        self.plainTextEditTest.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 110, 113, 20))
        self.spinBoxTest = QSpinBox(self.widget_3)
        self.spinBoxTest.setObjectName(u"spinBoxTest")
        self.spinBoxTest.setGeometry(QRect(520, 110, 51, 22))
        self.spinBoxTest.setDisplayIntegerBase(10)
        self.doubleSpinBoxTest = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBoxTest.setObjectName(u"doubleSpinBoxTest")
        self.doubleSpinBoxTest.setGeometry(QRect(580, 110, 62, 22))
        self.listViewTest = QListView(self.widget_3)
        self.listViewTest.setObjectName(u"listViewTest")
        self.listViewTest.setGeometry(QRect(660, 80, 201, 71))

        self.verticalLayout.addWidget(self.widget_3)


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


        self.retranslateUi(PageBogieModel)

        QMetaObject.connectSlotsByName(PageBogieModel)
    # setupUi

    def retranslateUi(self, PageBogieModel):
        PageBogieModel.setWindowTitle(QCoreApplication.translate("PageBogieModel", u"Form", None))
        self.labelTest.setText(QCoreApplication.translate("PageBogieModel", u"TextLabel", None))
        self.textEditAge.setDocumentTitle("")
        self.textEditAge.setPlaceholderText("")
        self.checkBoxTest.setText(QCoreApplication.translate("PageBogieModel", u"CheckBox", None))
        self.radioButtonTest1.setText(QCoreApplication.translate("PageBogieModel", u"RadioButton", None))
        self.radioButtonTest2.setText(QCoreApplication.translate("PageBogieModel", u"RadioButton", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("PageBogieModel", u"H:mm:ss", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("PageBogieModel", u"yyyy/M/d H:mm:ss", None))
        self.labelDateTimeTest.setText(QCoreApplication.translate("PageBogieModel", u"datetime show test", None))
        self.labelDateTest.setText(QCoreApplication.translate("PageBogieModel", u"date show test", None))
        self.labelTimeTest.setText(QCoreApplication.translate("PageBogieModel", u"time show test", None))
        self.pushButtonTest.setText(QCoreApplication.translate("PageBogieModel", u"PushButtonTest", None))
        self.plainTextEditTest.setPlainText(QCoreApplication.translate("PageBogieModel", u"111111\n"
"1222", None))
        self.pushButtonSave.setText(QCoreApplication.translate("PageBogieModel", u"PushButton", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("PageBogieModel", u"update", None))
        self.pushButtonadd.setText(QCoreApplication.translate("PageBogieModel", u"add", None))
        self.pushButtondelete.setText(QCoreApplication.translate("PageBogieModel", u"delete", None))
        self.pushButtoninsert.setText(QCoreApplication.translate("PageBogieModel", u"insert", None))
        self.pushButtonset.setText(QCoreApplication.translate("PageBogieModel", u"set", None))
        self.pushButtonclear.setText(QCoreApplication.translate("PageBogieModel", u"clear", None))
    # retranslateUi

