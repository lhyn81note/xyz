from libs.binding.dtobase import DtoBase

#绑定上下文
class Context:
    def __init__(self, ControlBindingList):
        self.context=None
        self.ControlBindingList=ControlBindingList
    def getContext(self):
        return self.context
    def setContext(self, value:DtoBase):
        self.context=value
        for binding in self.ControlBindingList:
            binding.setContext(value)