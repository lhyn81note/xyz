from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton
from PySide6.QtCore import Slot
import sys

class PathSelectorDialog(QDialog):
    """
    Dialog for selecting a path when multiple paths are available in the flow.
    """
    def __init__(self, current_node, paths, cmd_names, parent=None):
        """
        Initialize the dialog.
        
        Args:
            current_node (str): The current node ID
            paths (list): List of path IDs
            cmd_names (dict): Dictionary mapping command IDs to command names
            parent: Parent widget
        """
        super().__init__(parent)
        
        self.paths = paths
        self.cmd_names = cmd_names
        self.selected_path = None
        
        self.setWindowTitle(f"选择路径 - 当前节点: {current_node}")
        self.setModal(True)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QVBoxLayout(self)
        
        # Instruction label
        label = QLabel("请选择下一步执行的路径:")
        layout.addWidget(label)
        
        # Path selection combobox
        self.path_combo = QComboBox()
        for i, path_id in enumerate(self.paths):
            display_text = f"{i+1}. {path_id}"
            if path_id in self.cmd_names:
                display_text += f" - {self.cmd_names[path_id]}"
            self.path_combo.addItem(display_text, path_id)
        layout.addWidget(self.path_combo)
        
        # Confirm button
        confirm_button = QPushButton("确认")
        confirm_button.clicked.connect(self.on_confirm)
        layout.addWidget(confirm_button)
        
        # Cancel button
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)
        
        self.setLayout(layout)
        self.resize(300, 150)
        
    def on_confirm(self):
        """Handle confirm button click."""
        index = self.path_combo.currentIndex()
        if index >= 0:
            self.selected_path = self.paths[index]
        self.accept()
        
    def get_selected_path(self):
        """
        Get the selected path ID.
        
        Returns:
            str: The selected path ID or None if no selection was made
        """
        return self.selected_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flow Execution Example")
        self.resize(800, 600)
        
        # Initialize your UI components here
        
        # Setup CmdManager
        from libs.cmd import CmdMananger
        self.cmd_manager = CmdMananger("runtime/flows/test_path_selection.json", None)
        
        # Connect to the path selection signal
        self.cmd_manager.evtPathSelection.connect(self.on_path_selection_requested)
    
    @Slot(str, list, dict)
    def on_path_selection_requested(self, current_node, paths, cmd_names):
        """
        Handle path selection request from the flow execution.
        
        Args:
            current_node (str): The current node ID
            paths (list): List of available path IDs
            cmd_names (dict): Dictionary mapping command IDs to command names
        """
        print(f"Path selection requested for node {current_node}")
        print(f"Available paths: {paths}")
        
        # Create and show the dialog
        dialog = PathSelectorDialog(current_node, paths, cmd_names, self)
        
        if dialog.exec():
            selected_path = dialog.get_selected_path()
            print(f"User selected path: {selected_path}")
            
            # Call the callback function to continue the flow execution
            if hasattr(self.cmd_manager, 'path_selection_callback'):
                self.cmd_manager.path_selection_callback(selected_path)
        else:
            print("User canceled path selection")
            # Call the callback with None to indicate cancellation
            if hasattr(self.cmd_manager, 'path_selection_callback'):
                self.cmd_manager.path_selection_callback(None)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
