from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt,QEvent,QDateTime,QDate,QTime,QLocale

import os,sys
_top = sys.modules['__main__']
from view.template_bindpage._view import  Ui_PageBogieModel

from libs.binding.dtobase import DtoBase
from libs.binding.context import Context
from libs.binding.relayCommand import RelayCommand

from libs.binding.tableViewbinding import TableViewBinding
from libs.binding.tableWidgetbinding import TableWidgetBinding
from libs.binding.tableViewColumn import TableViewColumn
from libs.binding.bind import Bind
from libs.binding.bindingMode import BindingMode
from libs.binding.observableCollection import ObservableCollection
from libs.binding.textEditBinding import TextEditBinding
from libs.binding.labelBinding import LabelBinding
from libs.binding.checkBoxBinding import CheckBoxBinding
from libs.binding.radioButtonBinding import RadioButtonBinding
from libs.binding.dateTimeEditBinding import DateTimeEditBinding
from libs.binding.dateEditBinding import DateEditBinding
from libs.binding.timeEditBinding import TimeEditBinding
from libs.binding.comboBoxBinding import ComboBoxBinding
from libs.binding.pushButtonBinding import PushButtonBinding
from libs.binding.plainTextEditBinding import PlainTextEditBinding
from libs.binding.spinBoxBinding import SpinBoxBinding
from libs.binding.doubleSpinBoxBinding import DoubleSpinBoxBinding
from libs.binding.listViewBinding import ListViewBinding

class PageBogieModel(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_PageBogieModel()
        self.ui.setupUi(self)
        self.ui.pushButtonSave.clicked.connect(self.InitData)
        self.ui.pushButtonadd.clicked.connect(self.add)
        self.ui.pushButtoninsert.clicked.connect(self.insert)
        self.ui.pushButtondelete.clicked.connect(self.delete)
        self.ui.pushButtonclear.clicked.connect(self.clear)
        self.ui.pushButtonset.clicked.connect(self.set)
        self.ui.pushButtonUpdate.clicked.connect(self.update)
        self.context:Context=None
        self.InitData()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.FocusOut :
            a=1
            b=1
        return super().eventFilter(source, event)
    def update(self):
        strage=self.ui.textEditAge.toPlainText()
        self.dtoList[0].age=int(strage)
        None
    def add(self):
        data=TestDTO('x',1,'sssss')
        self.list.append(data)
    def insert(self):
        data=TestDTO('insert111',1,'sssss')
        self.list.insert(1,data)
    def delete(self):
        self.list.removeAt(0)
    def clear(self):
        self.list.clear()
    def set(self):
        data=TestDTO('xsetset',1,'sssss')
        self.list[0]=data

    def InitData(self):
        self.column=[
            TableViewColumn( '名称', 50,10, Qt.AlignmentFlag.AlignCenter,False ,None,Bind(None,None,'name')),
            TableViewColumn('IO', 50,10, Qt.AlignmentFlag.AlignRight ,False,None,Bind(None,None,'io')),
            # TableViewColumn('区',50,10, None ,False,None,Bind(None,None,'area')),
            # TableViewColumn('类型',50,10, None ,False,None,Bind(None,None,'type')),
            # TableViewColumn('地址',50,10, None ,False,None,Bind(None,None,'address')),
            # TableViewColumn('数值',50,10, None ,False,None,Bind(None,None,'value')),
        ]
        b = TableViewBinding(self.ui.tableView,self.column,Bind(None,"DataSource",'list',Mode=BindingMode.TwoWay))
        self.context=Context([b])

        self.datamodel=DataModel()
        # x=[DtoBase(jstr) for jstr in _top.PLC.config['pts']]
        # [print(_.name) for _ in x]
        # [print(dir(_)) for _ in x]
        y=[
            test("x",345),
            test("y",555)
        ]
        breakpoint()
        self.datamodel.list=ObservableCollection(y)
        self.context.setContext(self.datamodel)
 
class DataModel(DtoBase):
    def __init__(self):
        super().__init__()
        self.list:ObservableCollection=None

class test():
    name:str
    io:int
    def __init__(self,name,io):
        # super().__init__()
        self.name=name
        self.io=io
        