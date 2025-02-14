'''
@author: xue
@email: 497218754@qq.com
@version: 0.1
@license: Apache Licence
@file: dtodatalist.py
@time: 2019/12/10 10:20
@description: 
 基类为BaseDTO，子类继承该类，并实现其中的方法，即可实现DTO数据列表的功能。
'''
from PySide6.QtCore import  QObject, Signal
#数据列表
class ObservableCollection(QObject):

    collectionItemChangedSignal  = Signal(int, object,object)
    collectionDeleteSignal  = Signal( int,object)
    collectionInsertSignal  = Signal(int, object)
    collectionAppendSignal  = Signal( object)
    collectionClearSignal  = Signal()

    def __init__(self, list)->None:
        super().__init__()
        self.list = list

    def __len__(self):
        return len(self.list)
    def __getitem__(self, index):
        return self.list[index]

    def __setitem__(self, index, value):
        oldvalue=self.list[index]
        self.list[index] = value
        self.collectionItemChangedSignal.emit(index, value,oldvalue)

    def __delitem__(self, index):
        a=self.list[index]
        del self.list[index]
        self.collectionDeleteSignal.emit(index, a)
    def __iter__(self):
        return iter(self.list)

    def __contains__(self, value):
        return value in self.list
    def append(self, value):
        self.list.append(value)
        self.collectionAppendSignal.emit(value)
    def insert(self, index, value):
        if index<0 or index>=len(self.list):
            self.list.append(value)
            self.collectionAppendSignal.emit(value)
        else:
            self.list.insert(index, value)
            self.collectionInsertSignal.emit(index, value)
    def remove(self, value):
        if value not in self.list:
            raise ValueError("list.remove(x): x not in list")
        index=self.list.index(value)
        self.list.remove(value)
        self.collectionDeleteSignal.emit(index, value)
    def removeAt(self, index):
        if index<0 or index>=len(self.list):
            return
        value=self.list[index]
        self.list.remove(value)
        self.collectionDeleteSignal.emit(index, value)
    def pop(self, index=None):
        if index is None:
            return self.list.pop()
        else:
            return self.list.pop(index)

    def clear(self):
        self.list.clear()
        self.collectionClearSignal.emit()

    def index(self, value, start=None, end=None):
        return self.list.index(value, start, end)

    def count(self, value):
        return self.list.count(value)
    def sort(self, key=None, reverse=False):
        self.list.sort(key=key, reverse=reverse)

    def reverse(self):
        self.list.reverse()
    def copy(self):
        return ObservableCollection(self.list[:])
    def __str__(self):
        return str(self.list)
    
