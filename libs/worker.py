import time
import threading
from PySide6.QtCore import Qt, QObject, Signal

class WorkerSignals(QObject):
    show_dialog = Signal()
    update_label = Signal(str)

class Worker(threading.Thread):
    def __init__(self, signals):
        super().__init__()
        self.signals = signals
    
    def run(self):
        # Step 1: Wait 3 seconds in the worker thread
        time.sleep(1)
        # Step 2: Signal the main thread to show the dialog
        self.signals.show_dialog.emit()