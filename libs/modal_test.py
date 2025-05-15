import sys
from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, 
                               QPushButton, QDialogButtonBox)
from PySide6.QtCore import Qt, Signal

class CustomDialog(QDialog):
    # Add a signal to emit when dialog completes
    dialogFinished = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("模态对话框")
        self.setModal(True)  # 设置为模态对话框
        
        # 创建布局
        layout = QVBoxLayout(self)
        
        # 添加一些内容（可选）
        layout.addWidget(QPushButton("这是一个模态对话框示例"))
        
        # 创建按钮框
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.on_accepted)
        button_box.rejected.connect(self.on_rejected)
        
        layout.addWidget(button_box)
    
    def on_accepted(self):
        self.dialogFinished.emit(True)
        self.accept()
        
    def on_rejected(self):
        self.dialogFinished.emit(False)
        self.reject()
        
    def get_user_choice_async(self, callback):
        """Non-blocking dialog that calls callback with result"""
        self.dialogFinished.connect(callback)
        self.show()
