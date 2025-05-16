from libs.binding.bindingMode import  BindingMode
from PySide6.QtGui import QPalette,QColor
from PySide6.QtCore import QObject
from libs.binding.bind import    Bind
import re
#绑定控件基类
class ControlBaseBinding(QObject):
    #被绑定的控件对象，绑定列表
    def __init__(self, control, *bindList):
        super().__init__()
        self.control = control
        self.binds =  []
        for bind in bindList:
            if bind.widget is None:
                bind.widget = self
            self.binds.append(bind)
        self.context = None
         #命令属性
        self._command = None
    def setBind(self,*bindList):
        self.binds = []
        for bind in bindList:
            if bind.widget is None:
                bind.widget = self
            self.binds.append(bind)
    def getBind(self,property):
        for bind in self.binds:
            if bind.property == property:
                return bind
        return None
    def setBindList(self,bindList):
        self.binds = []
        for bind in bindList:
            if bind.widget is None:
                bind.widget = self
            self.binds.append(bind)
    def setContext(self, context):
        if self.context is not None:
            self.context.propertyChangedSignal.disconnect(self.onPropertyChanged)
        self.context = context

        for bind in self.binds:
            if not bind.property  is None:
                value = getattr(context, bind.ElementName)
                setattr(self,bind.property,value)
        self.context.propertyChangedSignal.connect(self.onPropertyChanged)
        
    def onPropertyChanged(self,  dto, name, value):
        for bind in self.binds:
            if bind.ElementName == name and (bind.Mode==BindingMode.OneWay or bind.Mode==BindingMode.TwoWay):
                oldvalue = getattr(self, bind.property)
                if oldvalue==value:
                    break
                setattr(self, bind.property, value)
                break
    def updateData(self,property,value):
        if self.context is None:
            return
        for bind in self.binds:
            if bind.property == property:
                if bind.Mode == BindingMode.TwoWay or bind.Mode == BindingMode.OneWayToSource:
                    oldvalue=getattr(self.context,bind.ElementName)
                    valtype=type(oldvalue)
                    try:
                        a=valtype(value)
                        setattr(self.context, bind.ElementName, a)
                    except:
                        raise ValueError("类型转换错误")
                return
    def getBindExtendData(self,property,key):
        for bind in self.binds:
            if bind.property == property:
                return bind.getData(key)
        return None
    #可见属性
    @property
    def Visible(self):
        return self.control.isVisible()
    
    @Visible.setter
    def Visible(self, value):
        self.control.setVisible(value)
    #使能属性
    @property
    def Enabled(self):
        return self.control.isEnabled()
    
    @Enabled.setter
    def Enabled(self, value):
        self.control.setEnabled(value)
    #位置属性
    @property
    def Location(self):
        return self.control.pos()
    
    @Location.setter
    def Location(self, value):
        self.control.move(value[0], value[1])
    #尺寸属性
    @property
    def Size(self):
        return self.control.size()
    
    @Size.setter
    def Size(self, value):
        self.control.resize(value[0], value[1])
    #标题属性
    @property
    def Title(self):
        return self.control.windowTitle()
    
    @Title.setter
    def Title(self, value):
        self.control.setWindowTitle(value)

    #背景色属性
    @property
    def BackgroundColor(self):
        return self.control.palette().color(QPalette.ColorRole.Base)
    
    @BackgroundColor.setter
    def BackgroundColor(self, value):
        css_values = {}
        css_pattern = r"(\w+-\w+|\w+):\s*(.*?);\s*"
        stylesheet = self.control.styleSheet()
        matches = re.finditer(css_pattern, stylesheet+ ";")
        for match in matches:
            property_name, value1 = match.groups()
            if property_name == "font":
                css_values[property_name]=value1
            else:
                rgb_values = re.sub(r"rgb\s*\(\s*|\s*\)", "", value1).split(",")
                # 转换为整数元组
                rgb = tuple(map(int, rgb_values))
                css_values[property_name]=rgb
        # 设置背景色
        cssnewValue = f"background-color: rgb({value[0]},{value[1]},{value[2]})"
        for property_name, value1 in css_values.items():
            if property_name == "font":
                cssnewValue += f";{property_name}: {value1}"
            elif property_name != "background-color":
                cssnewValue += f";\n{property_name}: rgb({value1[0]},{value1[1]},{value1[2]})"

        self.control.setStyleSheet(cssnewValue)
        return
        pallet = self.control.palette()
        pallet.setColor(QPalette.ColorRole.Base, QColor.fromRgb(value[0], value[1], value[2]))
        self.control.setPalette(pallet)
        self.control.setAutoFillBackground(True)


    #字体颜色属性
    @property
    def ForegroundColor(self):
        return self.control.palette().color(QPalette.ColorRole.Text)
    
    @ForegroundColor.setter
    def ForegroundColor(self, value):
        css_values = {}
        css_pattern = r"(\w+-\w+|\w+):\s*(.*?);\s*"
        stylesheet = self.control.styleSheet()
        matches = re.finditer(css_pattern, stylesheet+ ";")
        for match in matches:
            property_name, value1 = match.groups()
            if property_name == "font":
                css_values[property_name]=value1
            else:
                rgb_values = re.sub(r"rgb\s*\(\s*|\s*\)", "", value1).split(",")
                # 转换为整数元组
                rgb = tuple(map(int, rgb_values))
                css_values[property_name]=rgb
        # 设置背景色
        cssnewValue = f"color: rgb({value[0]},{value[1]},{value[2]})"
        for property_name, value1 in css_values.items():
            if property_name == "font":
                cssnewValue += f";{property_name}: {value1}"
            elif property_name != "color":
                cssnewValue += f";\n{property_name}: rgb({value1[0]},{value1[1]},{value1[2]})"

        self.control.setStyleSheet(cssnewValue)
        return
        pallet = self.control.palette()
        pallet.setColor(QPalette.ColorRole.Text, QColor.fromRgb(value[0], value[1], value[2]))
        self.control.setPalette(pallet)
        self.control.setAutoFillBackground(True)
   
    @property
    def Command(self):
        return self._command
    
    @Command.setter
    def Command(self, value):
        self._command = value
    @property
    def CommandParameter(self):
        bind=self.getBind("Command")
        if bind is None:
            return None
        return bind.getData("CommandParameter")
