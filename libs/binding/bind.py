from PySide6.QtWidgets import QWidget
from libs.binding.iValueConverter import IValueConverter
from libs.binding.bindingMode import BindingMode
#绑定类 widget为对应控件封装binding的类对象，可以为None，property为控件的属性名，ElementName为绑定元素的名称，
# **kwargs为其他参数，包括ConverterParameter为转换器参数，Converter为值转换器，Mode为绑定模式，CommandParameter为命令参数，OtherData为其他数据，ItemDelegate为itemdelegate
class Bind:
    def __init__(self, widget,property,ElementName:str,  **kwargs):
        self.widget = widget
        self.property = property
        self.ElementName = ElementName
        self.kwargs = kwargs
        
        self.data={ key:value for key, value in kwargs.items()}
        if  "Mode" not in self.data.keys():
            self.Mode = BindingMode.Default 
    @property
    def Converter(self)->IValueConverter:
        return self.data["Converter"] if "Converter" in self.data else None
    
    @Converter.setter
    def Converter(self,value:IValueConverter):
        if not isinstance(value,IValueConverter):
            raise ValueError("Converter must be an instance of IValueConverter")
        if "Converter" in self.data:
            raise ValueError("Converter already set")
        self.data["Converter"] = value 
    @property
    def ConverterParameter(self)->object:
        return self.data["ConverterParameter"] if "ConverterParameter" in self.data else None
    
    @ConverterParameter.setter
    def ConverterParameter(self,value:object):
        if "ConverterParameter" in self.data:
            raise ValueError("ConverterParameter already set")
        self.data["ConverterParameter"] = value
    
    @property
    def Mode(self)->BindingMode:
        return self.data["Mode"] if "Mode" in self.data else BindingMode.Default
    
    @Mode.setter
    def Mode(self,value:BindingMode):
        if not isinstance(value,BindingMode):
            raise ValueError("Mode must be an instance of BindingMode")
        if "Mode" in self.data:
            raise ValueError("Mode already set")
        self.data["Mode"] = value 

    @property
    def CommandParameter(self)->object:
        return self.data["CommandParameter"] if "CommandParameter" in self.data else None
    
    @CommandParameter.setter
    def CommandParameter(self,value:object):
        if "CommandParameter" in self.data:
            raise ValueError("CommandParameter already set")
        self.data["CommandParameter"] = value
    @property
    def OtherData(self)->object :
        return self.data["OtherData"] if "OtherData" in self.data else None
    
    @OtherData.setter
    def OtherData(self,value:object):
        if not isinstance(value,object):
            raise ValueError("OtherData must be an instance of IValueConverter")
        if "Converter" in self.data:
            raise ValueError("OtherData already set")
        self.data["OtherData"] = value 

    ###设置tableview列的itemdelegate，包括combobox、checkbox、dateedit、timeedit、datetimeedit等
    @property
    def ItemDelegate(self) :
        return self.data["ItemDelegate"] if "ItemDelegate" in self.data else None
    
    @ItemDelegate.setter
    def ItemDelegate(self,value):
        if "ItemDelegate" in self.data:
            raise ValueError("ItemDelegate already set")
        self.data["ItemDelegate"] = value
    def getData(self,key:str):
        if key in self.data.keys():
            return self.data[key]
        else:
            return None
if __name__ == "__main1__":
    b=Bind(None,"property","ElementName",Converter=None,Mode=BindingMode.TwoWay)
    print(b.Converter)
    print(b.Mode)