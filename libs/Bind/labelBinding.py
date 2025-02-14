from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#label控件绑定类
class LabelBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
    @property
    def Text(self):
        return self.control.text()
    
    @Text.setter
    def Text(self, value):
        self.control.setText(str(value))