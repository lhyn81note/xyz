from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from libs.Bind.bind import Bind
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
class ComboBoxBinding(ControlBaseBinding):
    
    def __init__(self, widget, *bindList):
        super().__init__(widget, *bindList)
        self.control.currentIndexChanged.connect(self.oncurrentIndexChanged)
        self.control.installEventFilter(self)
    def oncurrentIndexChanged(self, index):
        self.updateData("currentIndex",self.currentIndex)
        self.updateData("currentText",self.currentText)
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.FocusOut and source == self.control :
            self.updateData("currentIndex",self.currentIndex)
            self.updateData("currentText",self.currentText)
        return super().eventFilter(source, event)

    @property
    def currentIndex(self):
        return self.control.currentIndex()

    @currentIndex.setter
    def currentIndex(self, value):
        self.control.setCurrentIndex(value)

    @property
    def currentText(self):
        return self.control.currentText()

    @currentText.setter
    def currentText(self, value):
        self.control.setCurrentText(value)
    @property
    def Items(self):
        return self.control.Items    

    @Items.setter
    def Items(self, value):
        self.control.clear()
        self.control.addItems(value)
    @property
    def Model(self):
        return self.control.model()

    @property
    def displayProperty(self):
        return self.getBindExtendData("displayProperty")
    @property
    def valueProperty(self):
        return self.getBindExtendData("valueProperty")
    @Model.setter
    def Model(self, value):
        self.control.setModel(value)
   