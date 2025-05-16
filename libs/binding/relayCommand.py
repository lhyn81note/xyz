from libs.binding.icommand import ICommand
import typing
#实现按钮处理程序的类
class RelayCommand(ICommand):
    def __init__(self,executeFunc,canExecuteFunc=None):
        super().__init__()
        self.executeFunc = executeFunc
        self.canExecuteFunc = canExecuteFunc
    def Execute(self, parameter):
        if self.executeFunc is None:
            return
        self.executeFunc(parameter)
    def CanExecute(self, parameter):
        if self.canExecuteFunc is None:
            return True
        return self.canExecuteFunc(parameter)