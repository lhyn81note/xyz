from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#日期k时间控件绑定
class DateTimeEditBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.dateTimeChanged.connect(self.onDateTimeChanged)
        self.control.dateChanged.connect(self.onDateChanged)
        self.control.timeChanged.connect(self.onTimeChanged)    
    def onDateTimeChanged(self, dateTime):
        self.updateData( "DateTime", dateTime.toString("yyyy-MM-dd HH:mm:ss"))
    
    def onDateChanged(self, date):
        self.updateData( "Date", date.toString("yyyy-MM-dd"))
    
    def onTimeChanged(self, time):
        self.updateData( "Time", time.toString("HH:mm:ss"))
    @property
    def DateTime(self):
        return self.control.dateTime().toString("yyyy-MM-dd HH:mm:ss")
    
    @DateTime.setter
    def DateTime(self, value):
        self.control.setDateTime(QDateTime.fromString(value, "yyyy-MM-dd HH:mm:ss"))

    @property
    def Date(self):
        return self.control.date().toString("yyyy-MM-dd")
    
    @Date.setter
    def Date(self, value):
        self.control.setDate(QDate.fromString(value, "yyyy-MM-dd"))

    @property
    def Time(self):
        return self.control.time().toString("HH:mm:ss")
    
    @Time.setter
    def Time(self, value):
        self.control.setTime(QTime.fromString(value, "HH:mm:ss"))
    