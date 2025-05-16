from abc import ABC, abstractmethod
#绑定元素值与显示到控件上的转换接口
class IValueConverter(ABC):
    @abstractmethod
    def convert(self,  value:object, targetType:type, parameter:object):
        pass    
    @abstractmethod
    def convertBack(self,  value:object, targetType:type, parameter:object):
        pass