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

from view.setting_types._view import Ui_Form

class Window(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.context:Context=None
        self.InitData()

    def InitData(self):

        self.datamodel=DtoBase()

        # 设置0
        self.table0=[
            TableViewColumn( 'zxjxh', 50,10, Qt.AlignmentFlag.AlignCenter,False ,None,Bind(None,None,'zxjxh')),
            TableViewColumn('zxjgd', 50,10, Qt.AlignmentFlag.AlignRight ,False,None,Bind(None,None,'zxjgd')),
            TableViewColumn('Jzt1hxwy',50,10, None ,False,None,Bind(None,None,'Jzt1hxwy')),
            TableViewColumn('Jzt2hxwy',50,10, None ,False,None,Bind(None,None,'Jzt2hxwy')),
            TableViewColumn('Jzt1kjcxwy',50,10, None ,False,None,Bind(None,None,'Jzt1kjcxwy')),
            TableViewColumn('Jzt2kjcxwy',50,10, None ,False,None,Bind(None,None,'Jzt2kjcxwy')),
            TableViewColumn('FullLoadK',50,10, None ,False,None,Bind(None,None,'FullLoadK')),
            TableViewColumn('Jzt1Kzl',50,10, None ,False,None,Bind(None,None,'Jzt1Kzl')),
            TableViewColumn('Jzt2Kzl',50,10, None ,False,None,Bind(None,None,'Jzt2Kzl')),
        ]
        dtos0=[]
        items = _top.TblBogieType.Handler.getAll()
        for item in items:
            dtos0.append(item.dto())
        self.datamodel.table0=ObservableCollection(dtos0)   

        # 设置1
        self.table1=[
            TableViewColumn( 'zxjxh', 50,10, Qt.AlignmentFlag.AlignCenter,False ,None,Bind(None,None,'zxjxh')),
            TableViewColumn('sybwbh', 50,10, Qt.AlignmentFlag.AlignRight ,False,None,Bind(None,None,'sybwbh')),
            TableViewColumn('sybwmc',50,10, None ,False,None,Bind(None,None,'sybwmc')),
            TableViewColumn('stdValue',50,10, None ,False,None,Bind(None,None,'stdValue')),
            TableViewColumn('diffUp',50,10, None ,False,None,Bind(None,None,'diffUp')),

        ]
        dtos1=[]
        items = _top.TblBogiePosi.Handler.getAll()
        for item in items:
            dtos1.append(item.dto())
        self.datamodel.table1=ObservableCollection(dtos1)   

        # 设置0
        self.table2=[
            TableViewColumn( 'CRHxh', 50,10, Qt.AlignmentFlag.AlignCenter,False ,None,Bind(None,None,'CRHxh')),
            TableViewColumn('chNo0', 50,10, Qt.AlignmentFlag.AlignRight ,False,None,Bind(None,None,'chNo0')),
            TableViewColumn('chNo1',50,10, None ,False,None,Bind(None,None,'chNo1')),
            TableViewColumn('BogieNo',50,10, None ,False,None,Bind(None,None,'BogieNo')),
            TableViewColumn('Loadf1',50,10, None ,False,None,Bind(None,None,'Loadf1')),
            TableViewColumn('Loadf2',50,10, None ,False,None,Bind(None,None,'Loadf2')),
        ]
        dtos2=[]
        items = _top.TblBogieLoaderInfo.Handler.getAll()
        for item in items:
            dtos2.append(item.dto())
        self.datamodel.table2=ObservableCollection(dtos2)   

        # Set context
        self.context = Context([
            TableViewBinding(self.ui.tableView,self.table0,Bind(None,"DataSource",'table0',Mode=BindingMode.TwoWay)),
            TableViewBinding(self.ui.tableView_2,self.table1,Bind(None,"DataSource",'table1',Mode=BindingMode.TwoWay)),
            TableViewBinding(self.ui.tableView_3,self.table2,Bind(None,"DataSource",'table2',Mode=BindingMode.TwoWay)),
        ])
        self.context.setContext(self.datamodel)
       
        