from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Slot
import sys
import asyncio
import threading

# Import our classes
from libs.cmd import CmdMananger
from libs.path_selector import PathSelectorDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flow Execution Example")
        self.resize(800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        # Create test button
        self.test_button = QPushButton("Run Flow")
        self.test_button.clicked.connect(self.on_run_flow)
        layout.addWidget(self.test_button)
        
        # Set central widget
        self.setCentralWidget(central_widget)
        
        # Setup CmdManager
        self.cmd_manager = CmdMananger("runtime/flows/test.json", None)
        
        # Connect to the path selection signal
        self.cmd_manager.evtPathSelection.connect(self.on_path_selection_requested)
        
        # Store active dialogs to prevent garbage collection
        self.active_dialogs = {}
    
    @Slot()
    def on_run_flow(self):
        """Handle run flow button click."""
        self.test_button.setEnabled(False)
        self.cmd_manager.runflow()
    
    @Slot(str, list, dict)
    def on_path_selection_requested(self, current_node, paths, cmd_names):
        """
        Handle path selection request from the flow execution.
        
        Args:
            current_node (str): The current node ID
            paths (list): List of available path options
            cmd_names (dict): Dictionary mapping command IDs to command names (may be empty)
        """
        print(f"Path selection requested for node {current_node}")
        print(f"Available paths: {paths}")
        
        # Create and show the dialog
        dialog = PathSelectorDialog(paths, self)
        
        # Store the dialog to prevent garbage collection
        dialog_id = f"dialog_{current_node}"
        self.active_dialogs[dialog_id] = dialog
        
        # Connect the signal to the callback in the CmdManager
        if hasattr(self.cmd_manager, 'path_selection_callback'):
            dialog.evtReturn.connect(self.cmd_manager.path_selection_callback)
        
        # Connect to our own slot to clean up the dialog
        dialog.finished.connect(lambda: self.cleanup_dialog(dialog_id))
        
        # Show the dialog
        dialog.show()
    
    def cleanup_dialog(self, dialog_id):
        """Remove the dialog from our active dialogs dictionary."""
        if dialog_id in self.active_dialogs:
            del self.active_dialogs[dialog_id]
            print(f"Dialog {dialog_id} cleaned up")
            
            # Re-enable the button when all dialogs are closed
            if not self.active_dialogs:
                self.test_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
