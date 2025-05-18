from PySide6.QtCore import QObject, Signal
import logging

# 导入所有的弹窗类
from view.pops.path.view import Dialog as DialogPath
from view.pops.chart.view import Dialog as DialogChart

# 弹窗表映射
dialogMap = {
    "dialogPath": DialogPath,
    "dialogChart": DialogChart,
}

class Popup(QObject):

    evtBegin = Signal(str, dict, dict) # (id, args, lastResult/input)
    evtEnd = Signal(str, dict)

    def __init__(self):

        super().__init__()
        self.done = False
        self.result = None # 默认结果为None

    def pop(self, funcID, dialog_args, input=None):
        
        # def core():
        self.done = False
        theDialog = dialogMap[funcID](None, dialog_args, input)
        theDialog.exec()
        self.result = theDialog.get_result() # 这里有结果了
        self.done = True # 通知CmdManager弹窗任务完成

        # 注意这里不能采用多线程, 否则会卡死在Dialog窗口
        # thread = threading.Thread(target=core, daemon=True)
        # thread.start()


