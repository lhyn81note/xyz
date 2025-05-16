from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt,QEvent,QDateTime,QDate,QTime,QLocale

import os,sys
_top = sys.modules['__main__']
from libs.binding.relayCommand import RelayCommand
from libs.binding.context import Context
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

from libs.binding.tableViewbinding import TableViewBinding
from libs.binding.tableWidgetbinding import TableWidgetBinding
from libs.binding.tableViewColumn import TableViewColumn
from libs.binding.bind import Bind
from libs.binding.bindingMode import BindingMode
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

from view.db_users._view import Ui_Form

class Window(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        # self.ui.pushButtonSave.clicked.connect(self.InitData)
        # self.ui.pushButtonadd.clicked.connect(self.add)
        # self.ui.pushButtoninsert.clicked.connect(self.insert)
        # self.ui.pushButtondelete.clicked.connect(self.delete)
        # self.ui.pushButtonclear.clicked.connect(self.clear)
        # self.ui.pushButtonset.clicked.connect(self.set)
        self.ui.pushButtonUpdate.clicked.connect(self.update)
        self.context:Context=None
        self.InitData()

    # def eventFilter(self, source, event):
    #     if event.type() == QEvent.Type.FocusOut :
    #         a=1
    #         b=1
    #     return super().eventFilter(source, event)
    def update(self):
        for item in self.datamodel.table1:
            entity = _top.FaultCode.Entity()

            
    #     None
    # def add(self):
    #     data=TestDTO('x',1,'sssss')
    #     self.list.append(data)
    # def insert(self):
    #     data=TestDTO('insert111',1,'sssss')
    #     self.list.insert(1,data)
    # def delete(self):
    #     self.list.removeAt(0)
    # def clear(self):
    #     self.list.clear()
    # def set(self):
    #     data=TestDTO('xsetset',1,'sssss')
    #     self.list[0]=data

    def InitData(self):

        self.datamodel=DtoBase()

        # User
        self.table1=[
            TableViewColumn( '用户名', 50,10, Qt.AlignmentFlag.AlignCenter,False ,None,Bind(None,None,'UserName')),
            TableViewColumn('密码', 50,10, Qt.AlignmentFlag.AlignRight ,False,None,Bind(None,None,'LoginPassword')),
            TableViewColumn('用户类型',50,10, None ,False,None,Bind(None,None,'UserClass')),
        ]
        Bridge_User = TableViewBinding(self.ui.tableView,self.table1,Bind(None,"DataSource",'table1',Mode=BindingMode.TwoWay))
        dtos_1=[]
        items = _top.TblUser.Handler.getAll()
        for item in items:
            dtos_1.append(item.dto())
        self.datamodel.table1=ObservableCollection(dtos_1) 

        # Set context
        self.context = Context([Bridge_User])
        self.context.setContext(self.datamodel)
       
        