import sys
import time
import threading
import tracemalloc
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox
from PySide6.QtCore import Qt, QObject, Signal

class SubDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sub Dialog")
        self.setModal(True)
        self.setFixedSize(200, 150)
        
        layout = QVBoxLayout()
        
        self.combobox = QComboBox()
        self.combobox.addItems(["Apple", "Banana", "Orange"])
        self.combobox.setCurrentIndex(0)
        
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        
        layout.addWidget(QLabel("Select an item:"))
        layout.addWidget(self.combobox)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)
        
        self.confirm_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
    
    def get_selected_item(self):
        return self.combobox.currentText()

class WorkerSignals(QObject):
    show_dialog = Signal()
    update_label = Signal(str)

class Worker(threading.Thread):
    def __init__(self, signals):
        super().__init__()
        self.signals = signals
    
    def run(self):
        # Step 1: Wait 3 seconds in the worker thread
        time.sleep(3)
        # Step 2: Signal the main thread to show the dialog
        self.signals.show_dialog.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setFixedSize(300, 150)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        
        self.label = QLabel("No choice yet")
        self.button = QPushButton("Start Process")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.central_widget.setLayout(layout)
        
        self.button.clicked.connect(self.start_process)
        
        # Setup signals
        self.signals = WorkerSignals()
        self.signals.show_dialog.connect(self.show_dialog)
        self.signals.update_label.connect(self.label.setText)
    
    def start_process(self):
        self.button.setEnabled(False)
        self.label.setText("Waiting 3 seconds...")
        
        # Start worker thread
        self.worker = Worker(self.signals)
        self.worker.start()
    
    def show_dialog(self):
        try:
            dialog = SubDialog(self)
            result = dialog.exec()
            # print(f"Dialog result: {result}")
            
            if result == QDialog.Accepted:
                choice = dialog.get_selected_item()
                self.label.setText(f"Selected: {choice}")
            else:
                self.label.setText("Cancelled")
        finally:
            self.button.setEnabled(True)

if __name__ == "__main__":
    # Enable tracemalloc for debugging
    tracemalloc.start()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())