from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#控件复选框绑定
class CheckBoxBinding(ControlBaseBinding):
    #初始化 被绑定控件，绑定列表
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        # self.control.checkStateChanged.connect(self.onStateChanged)
        self.control.toggled.connect(self.onClicked)
    def onStateChanged(self, state):
        self.updateData( "Checked", state==Qt.CheckState.Checked)
    def onClicked(self, state):
         if self.Command is not None:
            if self.Command.CanExecute(self.CommandParameter):
                self.Command.Execute(self.CommandParameter)
    @property
    def Checked(self):
        return self.control.isChecked()
    
    @Checked.setter
    def Checked(self, value):
        self.control.setChecked(value)