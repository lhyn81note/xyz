from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#时间编辑器绑定类
class TimeEditBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.timeChanged.connect(self.onTimeChanged)    
    
    
    def onTimeChanged(self, time):
        self.updateData( "Time", time.toString("HH:mm:ss"))

    @property
    def Time(self):
        return self.control.time().toString("HH:mm:ss")
    
    @Time.setter
    def Time(self, value):
        self.control.setTime(QTime.fromString(value, "HH:mm:ss"))
    