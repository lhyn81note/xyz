from PySide6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QComboBox, QCheckBox


class Dialog(QDialog):
    def __init__(self, parent=None, dialog_args=None, input=None):

        super().__init__(parent)
        self.ret = None
        self.setWindowTitle("流程选择")
        self.setModal(True)
        self.setFixedSize(200, 150)

        layout = QVBoxLayout()

        self.combobox = QComboBox()
        self.combobox.addItems(dialog_args['next_cmds'])
        self.combobox.setCurrentIndex(0)

        self.addflag = QCheckBox("保留原路径并添加")
        self.addflag.setChecked(True)

        self.confirm_button = QPushButton("确认")
        self.cancel_button = QPushButton("取消")

        layout.addWidget(QLabel("可选流程:"))
        layout.addWidget(self.combobox)
        layout.addWidget(self.addflag)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.confirm_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def ok(self):
        self.ret = self.combobox.currentText()
        self.ret += f":{self.addflag.isChecked()}"  # Add flag to result string
        self.accept()

    def cancel(self):
        self.ret = None
        self.reject()

    def get_result(self):
        return self.ret
