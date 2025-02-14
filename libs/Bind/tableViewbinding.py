
from PySide6.QtGui import QStandardItemModel,QStandardItem
from libs.Bind.observableCollection import ObservableCollection
from libs.Bind.tableViewColumn import TableViewColumn
from libs.Bind.bindingMode import BindingMode
from libs.Bind.controlBaseBinding import ControlBaseBinding
#表格视图绑定
class TableViewBinding(ControlBaseBinding):
    def __init__(self, tableView, columnlist,*bindList):
        super().__init__(tableView,*bindList)
        self.datalist = None
        self.columnlist = columnlist
        self.map = []
        self.viewModels=QStandardItemModel()
        self.tableView=tableView
        
        #生成列头
        self.HorizontalHeaderLabels=[ self.columnlist[i].header for i in range(len(self.columnlist))]
        self.viewModels.setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
       
        if self.tableView is not None:
            self.tableView.setModel(self.viewModels)
            for i in range(len(self.columnlist)):
                col:TableViewColumn=self.columnlist[i]
                if col.bind.ItemDelegate is not None:
                    self.tableView.setItemDelegateForColumn(i,col.bind.ItemDelegate)
    def OnPropertyChanged(self, sender, propName, value):
        for i in range(len(self.map)):
            mp=self.map[i]
            dto=mp[0]
            if dto==sender:
                for j in range(len(self.columnlist)):
                    col:TableViewColumn=self.columnlist[j]
                    if col.bind.ElementName==propName:
                        mode=col.bind.Mode
                        if mode==BindingMode.TwoWay or  mode==BindingMode.OneWay:
                            row=mp[1]
                            strvalue=''
                            if value is not None:
                                strvalue=str(value)
                            row[j].setText(strvalue)
                        return
    def OnCollectionClear(self):
        self.map=[]
        self.viewModels.clear()

    def OnCollectionInsert(self, index, value):
        
        if index<0 or index>=len(self.map):
            return
        row=[]
        dto=value
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
        self.map.insert(index,[dto,row])
        self.viewModels.insertRow(index,row)
        dto.propertyChangedSignal.connect(self.OnPropertyChanged)

    def OnCollectionAppend(self, value):
        row=[]
        dto=value
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
        dto.propertyChangedSignal.connect(self.OnPropertyChanged)
    def OnCollectionDelete(self, index,value):
        for i in range(len(self.map)):
            mp=self.map[i]
            if mp[0]==value:
                self.map.pop(i)
                index=self.viewModels.indexFromItem(mp[1][0])
                self.viewModels.removeRow(index.row())
                return

    

    def OnCollectionChanged( self, index, newvalue, oldvalue):
        for i in range(len(self.map)):
            mp=self.map[i]
            dto=mp[0]
            row=mp[1]
            if dto==oldvalue:
                for j in range(len(self.columnlist)):
                    col:TableViewColumn=self.columnlist[j]
                    if hasattr(newvalue,col.bind.ElementName):
                        propValue=getattr(newvalue,col.bind.ElementName)
                    strvalue=''
                    if propValue is not None:
                        strvalue=str(propValue)
                    row[j].setText(strvalue)
                mp[0]=newvalue
                newvalue.propertyChangedSignal.connect(self.OnPropertyChanged)    
                None

    def ChangeItem(self, item):
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
    

    def createModel(self, datalist: ObservableCollection):

        
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
            dto.propertyChangedSignal.connect(self.OnPropertyChanged)
        self.viewModels.itemChanged.connect(self.ChangeItem)
        self.datalist.collectionItemChangedSignal.connect(self.OnCollectionChanged)
        self.datalist.collectionDeleteSignal.connect(self.OnCollectionDelete)
        self.datalist.collectionAppendSignal.connect(self.OnCollectionAppend)
        self.datalist.collectionInsertSignal.connect(self.OnCollectionInsert)
        self.datalist.collectionClearSignal.connect(self.OnCollectionClear)
        if self.tableView is not None:
            self.tableView.setModel(self.viewModels)
            for i in range(len(self.columnlist)):
                col:TableViewColumn=self.columnlist[i]
                if col.bind.ItemDelegate is not None:
                    self.tableView.setItemDelegateForColumn(i,col.bind.ItemDelegate)
    @property
    def DataSource(self):
        return self.datalist
    @DataSource.setter
    def DataSource(self,value):

        if self.datalist is not None and len(self.datalist)> 0:
            self.datalist.collectionItemChangedSignal.disconnect(self.OnCollectionChanged)
            self.datalist.collectionDeleteSignal.disconnect(self.OnCollectionDelete)
            self.datalist.collectionAppendSignal.disconnect(self.OnCollectionAppend)
            self.datalist.collectionInsertSignal.disconnect(self.OnCollectionInsert)
            self.datalist.collectionClearSignal.disconnect(self.OnCollectionClear)
        self.datalist=value
        #datamodel
        self.createModel(self.datalist)
