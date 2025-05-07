# -*- coding: utf-8 -*-

from view.template_notify._view import Ui_Form
import os,sys
_top = sys.modules['__main__']
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QLabel
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from __main__ import *

class Window(QWidget):
    def __init__(self, menus=None, title=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if title:
            self.setWindowTitle(title)

        labels_layout = QVBoxLayout()
        label1 = QLabel("报警")
        label2 = QLabel("信息")
        label3 = QLabel("状态")
        labels_layout.addWidget(label1)
        labels_layout.addWidget(label2)
        labels_layout.addWidget(label3)
        
        buttons_layout = QVBoxLayout()
        btn1 = QPushButton("触发报警")
        btn2 = QPushButton("触发信息")
        btn3 = QPushButton("触发状态")
        buttons_layout.addWidget(btn1)
        buttons_layout.addWidget(btn2)
        buttons_layout.addWidget(btn3)

        btn1.clicked.connect(lambda: broker.publish(msg_type=MsgType.alarm, content="触发报警!"))
        btn2.clicked.connect(lambda: broker.publish(msg_type=MsgType.info, content="新消息!"))
        btn3.clicked.connect(lambda: broker.publish(msg_type=MsgType.status, content=True))
        
        self.ui.horizontalLayout_2.addLayout(buttons_layout)
        self.ui.horizontalLayout_2.addLayout(labels_layout)
        
        broker = _top.Broker
        broker.addSubscriber(MsgSubscriber(lambda msg: label1.setText(msg)), msg_type=MsgType.alarm)
        broker.addSubscriber(MsgSubscriber(lambda msg: label2.setText(msg)), msg_type=MsgType.info)
        broker.addSubscriber(MsgSubscriber(lambda msg: label3.setText("是" if msg else "否")), msg_type=MsgType.status)
        
