from enum import Enum,auto
#绑定数据元素与控件之间传输的方式
class BindingMode(Enum):
    #Data flows from source to target, source changes cause data flow
    OneWay= 1
    #Data flows from source to target and vice-versa
    TwoWay = 3
    #Data flows from target to source, target changes cause data flow
    OneWayToSource = 2
    #Data flows from source to target once, source changes are ignored
    OneTime = 0
    Default = -1
    
