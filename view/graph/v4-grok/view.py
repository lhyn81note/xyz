# -*- coding: utf-8 -*-
from _view import Ui_Form
import os,sys
# import ollama
# _top = sys.modules['__main__']
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,QThread,Signal,QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QMainWindow, QSizePolicy, QWidget, QDialog)
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import Slot, QUrl, QObject, QAbstractListModel, Qt, QSize, QMimeData
# import requests

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.qml_flow = QQuickWidget()
        self.qml_flow.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.qml_flow.setSource(QUrl.fromLocalFile('main-embed.qml'))
        self.qml_root = self.qml_flow.rootObject()
        self.layout_tags = QVBoxLayout(self.ui.wgt_flow)
        self.layout_tags.addWidget(self.qml_flow)


