from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#按钮绑定
class PushButtonBinding(ControlBaseBinding):
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.pressed.connect(self.onPressed)
    def onPressed(self):
        if self.Command is not None:
            if self.Command.CanExecute(self.CommandParameter):
                self.Command.Execute(self.CommandParameter)