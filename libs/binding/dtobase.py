import typing
from PySide6.QtCore import  QObject, Signal
import uuid,json
"""
绑定的数据模型均需要继承自该类
"""
class DtoBase(QObject):

    propertyChangedSignal  = Signal(object, str, object)
    # vlueChangedSignal = Signal(str, object)
    def __init__(self, jstr=None) -> object:
        super().__init__()

        if jstr:
            obj=None
            if isinstance(jstr, str):
                obj = json.loads(jstr)
            elif isinstance(jstr, dict):
                obj = jstr
            if obj:
                for key, value in obj.items():
                    setattr(self, key, value)

    def emitPropertyChanged(self, propertyName, value) -> None:
        self.vlueChangedSignal.emit(propertyName, value)

    def __setattr__(self, name: str, value: typing.Any) -> None:
        has= hasattr(self, name)
        if name in self.__dict__:
            prevalue = getattr(self, name)
            if prevalue == value:
                return
        super().__setattr__(name, value)
        self.propertyChangedSignal.emit(self, name, value)


class jsonparser():
    def __init__(self,jsonstr)-> object: 
        self.jsonstr = jsonstr
        if isinstance(jsonstr, str):
            obj = json.loads(jsonstr)
        elif isinstance(jsonstr, dict):
            obj = jsonstr
        else:
            raise TypeError("输入必须是JSON字符串或字典")          
        for key, value in obj.items():
            setattr(self, key, value)


