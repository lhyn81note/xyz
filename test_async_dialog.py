import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

# Import our CmdManager class
from libs.cmd import CmdMananger

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Async Dialog Test")
        self.resize(400, 300)
        
        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        # Create test button
        self.test_button = QPushButton("Test Dialog")
        self.test_button.clicked.connect(self.on_test_clicked)
        layout.addWidget(self.test_button)
        
        # Create a CmdManager instance
        self.cmd_manager = CmdMananger("runtime/flows/test.json", None)
        
        # Set central widget
        self.setCentralWidget(central_widget)
        
    def on_test_clicked(self):
        """Handle test button click."""
        print("Starting async dialog test...")
        self.test_button.setEnabled(False)
        
        # Start the async test in a non-blocking way
        QTimer.singleShot(0, self.run_async_test)
        
    def run_async_test(self):
        """Run the async test."""
        # Create and run the async task
        asyncio.run(self.async_test())
        
    async def async_test(self):
        """Async test function."""
        print("Showing dialog...")
        
        # Test with custom options
        options = ["Option A", "Option B", "Option C"]
        result = await self.cmd_manager.popup(args=options)
        
        print(f"Dialog result: {result}")
        self.test_button.setEnabled(True)
        
        if result:
            print("Dialog was accepted with a selection")
        else:
            print("Dialog was canceled or closed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
