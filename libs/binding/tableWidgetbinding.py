
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtWidgets import QTableWidgetItem,QTableWidget
from libs.binding.observableCollection import ObservableCollection
from libs.binding.tableViewColumn import TableViewColumn
from libs.binding.bindingMode import BindingMode
from libs.binding.controlBaseBinding import ControlBaseBinding
#表格widget绑定
class TableWidgetBinding(ControlBaseBinding):
    def __init__(self, tableWidget, columnlist,*bindList):
        super().__init__(tableWidget,*bindList)
        self.datalist = None
        self.columnlist = columnlist
        self.map = []
        self.viewModels=[]
        self.tableWidget:QTableWidget=tableWidget
        
        #生成列头
        self.HorizontalHeaderLabels=[ self.columnlist[i].header for i in range(len(self.columnlist))]
        
        #生成行
        self.tableWidget.itemChanged.connect(self.ChangeItem)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(self.columnlist))
        self.tableWidget.setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        pass
        
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
        self.delete_all_rows(self.tableWidget)
        pass

    def delete_all_rows(self, table_widget):
    # 获取表格中的行数
        row_count = table_widget.rowCount()
    # 从最后一行开始删除，以避免因删除行导致的行号变化问题
        for row in range(row_count - 1, -1, -1):
            table_widget.removeRow(row)
    def OnCollectionInsert(self, index, value):
        
        if index<0 or index>=len(self.map):
            return
        row=[]
        dto=value
        self.tableWidget.insertRow(index)
        for j in range(len(self.columnlist)):
            col:TableViewColumn=self.columnlist[j]
            if hasattr(dto,col.bind.ElementName):
                value=getattr(dto,col.bind.ElementName)
                strvalue=''
                if value is not None:
                    strvalue=str(value)
                item=QTableWidgetItem(strvalue)
                if col.align is not None:
                    item.setTextAlignment(col.align)
                row.append(item)
                self.tableWidget.setItem(index,j,item)
        self.map.insert(index,[dto,row])
        dto.propertyChangedSignal.connect(self.OnPropertyChanged)

    def OnCollectionAppend(self, value):
        row=[]
        dto=value
        rowcount=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowcount)
        for j in range(len(self.columnlist)):
            col:TableViewColumn=self.columnlist[j]
            if hasattr(dto,col.bind.ElementName):
                value=getattr(dto,col.bind.ElementName)
                strvalue=''
                if value is not None:
                    strvalue=str(value)
                item=QTableWidgetItem(strvalue)
                if col.align is not None:
                    item.setTextAlignment(col.align)
                row.append(item)
                self.tableWidget.setItem(rowcount,j,item)
        self.map.append([dto,row])
        dto.propertyChangedSignal.connect(self.OnPropertyChanged)
    def OnCollectionDelete(self, index,value):
        for i in range(len(self.map)):
            mp=self.map[i]
            if mp[0]==value:
                self.map.pop(i)
                self.tableWidget.removeRow(i)
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
                    propName=self.columnlist[j].bind.ElementName
                    oldvalue=getattr(dto,propName)
                    valtype=type(oldvalue)
                    try:
                        a=valtype(item.text())
                        setattr(dto,propName,a)
                    except:
                        raise ValueError("类型转换错误")
                    return
    
    def createModel(self,datalist):
        self.datalist = datalist
        self.map = []
        self.viewModels=[]
        
        #生成列头
        self.HorizontalHeaderLabels=[ self.columnlist[i].header for i in range(len(self.columnlist))]
        
        #生成行
        self.tableWidget.clear()
        self.tableWidget.itemChanged.disconnect(self.ChangeItem)
        self.tableWidget.setRowCount(len(datalist))
        self.tableWidget.setColumnCount(len(self.columnlist))
        self.tableWidget.setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
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
                    item=QTableWidgetItem(strvalue)
                    if col.align is not None:
                        item.setTextAlignment(col.align)
                    self.tableWidget.setItem(i,j,item)
                    row.append(item)
            self.map.append([dto,row])
            self.viewModels.append(row)
            dto.propertyChangedSignal.connect(self.OnPropertyChanged)
        self.tableWidget.itemChanged.connect(self.ChangeItem)
        self.datalist.collectionItemChangedSignal.connect(self.OnCollectionChanged)
        self.datalist.collectionDeleteSignal.connect(self.OnCollectionDelete)
        self.datalist.collectionAppendSignal.connect(self.OnCollectionAppend)
        self.datalist.collectionInsertSignal.connect(self.OnCollectionInsert)
        self.datalist.collectionClearSignal.connect(self.OnCollectionClear)
        pass
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