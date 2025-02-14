from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#富文本编辑框绑定
class PlainTextEditBinding(ControlBaseBinding):
    
    def __init__(self, textEdit, *bindList):
        super().__init__(textEdit, *bindList)
        #self.textEdit.textChanged.connect(self.onTextChanged)
        self.control.installEventFilter(self)
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.FocusOut and source == self.control :
            self.onTextChanged()
        return super().eventFilter(source, event)
    def onTextChanged(self):
        if self.context is None:
            return
        for bind in self.binds:
            if bind.property == "Text":
                if bind.Mode == BindingMode.TwoWay or bind.Mode == BindingMode.OneWayToSource:
                    value = self.control.toPlainText()
                    oldvalue=getattr(self.context,bind.ElementName)
                    valtype=type(oldvalue)
                    try:
                        a=valtype(value)
                        setattr(self.context, bind.ElementName, a)
                    except:
                        raise ValueError("类型转换错误")
                return    
    @property
    def Text(self):
        return self.control.toPlainText()
    
    @Text.setter
    def Text(self, value):
        if self.Text == str(value):
            return
        self.control.setPlainText(str(value))

    @property
    def ReadOnly(self):
        return self.control.isReadOnly()
    
    @ReadOnly.setter
    def ReadOnly(self, value):
        self.control.setReadOnly(value)
