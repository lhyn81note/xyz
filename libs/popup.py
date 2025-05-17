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

    evtBegin = Signal(str, dict)
    evtEnd = Signal(str, dict)

    def __init__(self):

        super().__init__()
        self.done = False
        self.result = None

    def pop(self, dialog_id, dialog_args):
        
        # def core():
        self.done = False
        theDialog = dialogMap[dialog_id](None, dialog_args)
        theDialog.exec()
        self.dialog_result = theDialog.get_result()
        self.done = True
        self.result = self.dialog_result

        # 注意这里不能采用多线程, 否则会卡死在Dialog窗口
        # thread = threading.Thread(target=core, daemon=True)
        # thread.start()


