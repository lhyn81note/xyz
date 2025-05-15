import sys
import time
import threading
import tracemalloc
from PySide6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QComboBox
from PySide6.QtCore import Signal, QObject


class Popup(QObject):

    evtBegin = Signal(str, dict)
    evtEnd = Signal(str, dict)

    def __init__(self):

        super().__init__()
        self.dialog_id = None
        self.dialog_args = None
        self.done = False
        self.result = None

    def pop(self, dialog_id, dialog_args):
        
        self.dialog_id = dialog_id
        self.dialog_args = dialog_args

        # def core():
        self.done = False

        # Create dialog without passing self as parent
        thedialog = TestDialog(None, dialog_args["next"])
        thedialog.exec()  # Blocking call to show the dialog
        print("Dialog opened")  
        self.dialog_result = thedialog.get_result()
        self.done = True
        self.result = self.dialog_result

        print("Dialog closed")

        # thread = threading.Thread(target=core, daemon=True)
        # thread.start()


class TestDialog(QDialog):
    def __init__(self, parent=None, next_cmd=[]):
        super().__init__(parent)
        self.ret = None
        self.setWindowTitle("Sub Dialog")
        self.setModal(True)
        self.setFixedSize(200, 150)

        layout = QVBoxLayout()

        self.combobox = QComboBox()
        self.combobox.addItems(next_cmd)
        self.combobox.setCurrentIndex(0)

        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")

        layout.addWidget(QLabel("Select an item:"))
        layout.addWidget(self.combobox)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.confirm_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def ok(self):
        self.ret = self.combobox.currentText()
        self.accept()

    def cancel(self):
        self.ret = None
        self.reject()

    def get_result(self):
        return self.ret
