from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton
from PySide6.QtCore import Qt, Signal

class PathSelectorDialog(QDialog):
    """
    Dialog for selecting a path when multiple paths are available in the flow.
    """
    pathSelected = Signal(int)  # Signal to emit the selected path index
    
    def __init__(self, paths, cmd_names, parent=None):
        """
        Initialize the dialog.
        
        Args:
            paths (list): List of path IDs
            cmd_names (dict): Dictionary mapping command IDs to command names
            parent: Parent widget
        """
        super().__init__(parent)
        
        self.paths = paths
        self.cmd_names = cmd_names
        self.selected_index = -1
        
        self.setWindowTitle("选择路径")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
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
        
        self.setLayout(layout)
        self.resize(300, 150)
        
    def on_confirm(self):
        """Handle confirm button click."""
        self.selected_index = self.path_combo.currentIndex()
        self.pathSelected.emit(self.selected_index)
        self.accept()
        
    def get_selected_path(self):
        """
        Get the selected path ID.
        
        Returns:
            str: The selected path ID or None if no selection was made
        """
        if self.selected_index >= 0 and self.selected_index < len(self.paths):
            return self.paths[self.selected_index]
        return None
