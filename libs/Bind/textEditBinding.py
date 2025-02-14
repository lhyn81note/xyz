from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#文本输入编辑框绑定
class TextEditBinding(ControlBaseBinding):
    
    def __init__(self, textEdit, *bindList):
        super().__init__(textEdit, *bindList)
        self.textEdit = textEdit
        #self.textEdit.textChanged.connect(self.onTextChanged)
        self.textEdit.installEventFilter(self)
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.FocusOut and source == self.textEdit :
            self.onTextChanged()
        return super().eventFilter(source, event)
    def onTextChanged(self):
        if self.context is None:
            return
        for bind in self.binds:
            if bind.property == "Text":
                if bind.Mode == BindingMode.TwoWay or bind.Mode == BindingMode.OneWayToSource:
                    value = self.textEdit.toPlainText()
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
        return self.textEdit.toPlainText()
    
    @Text.setter
    def Text(self, value):
        if self.Text == str(value):
            return
        self.textEdit.setPlainText(str(value))

    @property
    def ReadOnly(self):
        return self.textEdit.isReadOnly()
    
    @ReadOnly.setter
    def ReadOnly(self, value):
        self.textEdit.setReadOnly(value)
    @property
    def ForeColor(self):
        return self.textEdit.textColor()
    
    @ForeColor.setter
    def ForeColor(self, value):
        self.textEdit.setTextColor(value)
    @property
    def BackColor(self):
        return self.BackgroundColor
    
    @BackColor.setter
    def BackColor(self, value):
        self.BackgroundColor = value
    