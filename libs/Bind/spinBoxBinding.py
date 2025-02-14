from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#微调框绑定
class SpinBoxBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.valueChanged.connect(self.onValueChanged)
    def onValueChanged(self, value):
        self.updateData( "Value",value)
    @property
    def Value(self):
        return self.control.value()
    
    @Value.setter
    def Value(self, value):
        self.control.setValue(value)