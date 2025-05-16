from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.binding.bind import Bind
from libs.binding.bindingMode import BindingMode
from libs.binding.controlBaseBinding import ControlBaseBinding
#单选按钮绑定
class RadioButtonBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.toggled.connect(self.ontoggled)
        self.control.clicked.connect(self.onClicked)
    def ontoggled(self, checked):
        self.updateData( "Checked", checked)
    def onClicked(self,checked):
        if self.Command is not None:
            if self.Command.CanExecute(self.CommandParameter):
                self.Command.Execute(self.CommandParameter)
        pass
    @property
    def Checked(self):
        return self.control.isChecked()
    
    @Checked.setter
    def Checked(self, value):
        self.control.setChecked(value)