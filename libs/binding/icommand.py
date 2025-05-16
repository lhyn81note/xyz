from abc import ABC, abstractmethod
# 按钮命令接口
class ICommand:
    @abstractmethod
    def Execute(self,parameter):
        pass    
    @abstractmethod
    def CanExecute(self, parameter):
        pass
