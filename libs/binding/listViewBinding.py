
from PySide6.QtGui import QStandardItemModel,QStandardItem
from libs.binding.observableCollection import ObservableCollection
from libs.binding.tableViewColumn import TableViewColumn
from libs.binding.bindingMode import BindingMode
from libs.binding.controlBaseBinding import ControlBaseBinding
#表格视图绑定
class ListViewBinding(ControlBaseBinding):
    def __init__(self, tableView, columnlist,*bindList):
        super().__init__(tableView,*bindList)
        self.datalist = None
        self.columnlist = columnlist
        self.map = []
        self.viewModels=QStandardItemModel()
        
        #生成列头
        self.HorizontalHeaderLabels=[ self.columnlist[i].header for i in range(len(self.columnlist))]
        self.viewModels.setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
       
        if self.control is not None:
            self.control.setModel(self.viewModels)
           
   
    def createModel(self, datalist):

        self.datalist = datalist
        self.map = []
        self.viewModels=QStandardItemModel()
        
        #生成列头
        self.HorizontalHeaderLabels=[ self.columnlist[i].header for i in range(len(self.columnlist))]
        self.viewModels.setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        #生成行
        for i in range(len(datalist)):
            row=[]
            dto=datalist[i]
            for j in range(len(self.columnlist)):
                col:TableViewColumn=self.columnlist[j]
                if hasattr(dto,col.bind.ElementName):
                    value=getattr(dto,col.bind.ElementName)
                    strvalue=''
                    if value is not None:
                        strvalue=str(value)
                    item=QStandardItem(strvalue)
                    item.setEditable(not col.isReadOnly)
                    if col.align is not None:
                        item.setTextAlignment(col.align)
                    row.append(item)
            self.map.append([dto,row])
            self.viewModels.appendRow(row)
        self.viewModels.itemChanged.connect(self.ChangeItem)
        if self.control is not None:
            self.control.setModel(self.viewModels)
            self.control.setModelColumn(1)
    @property
    def DataSource(self):
        return self.datalist
    @DataSource.setter
    def DataSource(self,value):
        self.createModel(value)

    def ChangeItem(self, item):
        return
        for i in range(len(self.map)):
            mp=self.map[i]
            dto=mp[0]
            row=mp[1]
            for j in range(len(row)):
                if item==row[j]:
                    index=self.viewModels.indexFromItem(item)
                    col=index.column()
                    propName=self.columnlist[col].bind.ElementName
                    oldvalue=getattr(dto,propName)
                    valtype=type(oldvalue)
                    try:
                        a=valtype(item.text())
                        setattr(dto,propName,a)
                    except:
                        raise ValueError("类型转换错误")
                    return
    
