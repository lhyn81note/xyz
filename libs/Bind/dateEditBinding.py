from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#日期控件绑定类
class DateEditBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.dateChanged.connect(self.onDateChanged)
    def onDateChanged(self, date):
        self.updateData( "Date", date.toString("yyyy-MM-dd"))
    
   

    @property
    def Date(self):
        return self.control.date().toString("yyyy-MM-dd")
    
    @Date.setter
    def Date(self, value):
        self.control.setDate(QDate.fromString(value, "yyyy-MM-dd"))

    