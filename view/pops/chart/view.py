from view.pops.chart._view import Ui_Form
import os,sys
_top = sys.modules['__main__']
from PySide6.QtWidgets import  QDialog, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from __main__ import *

class Dialog(QDialog):
    def __init__(self, menus=None, title=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if title:
            self.setWindowTitle(title)

        self.plcdata = _top.PlcData(list(_top.PLC.pts.values()))
        plcview = _top.PlcTable(self.plcdata)
        # _top.PLC.register_callback(lambda ipt: self.plcdata.setData(ipt[0], 5, ipt[1]))
        _top.PLC.register_callback(lambda: self.plcdata.update())
        self.ui.horizontalLayout_2.addWidget(plcview)
