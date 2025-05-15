from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QApplication
from PySide6.QtCore import Qt, Signal

class PathSelectorDialog(QDialog):
    """
    Dialog for selecting a path when multiple paths are available in the flow.
    """
    evtReturn = Signal(object)  # Signal to emit the selected path

    def __init__(self, args, parent=None):
        """
        Initialize the dialog.

        Args:
            args (list): List of path options
            parent: Parent widget
        """
        # Find the main window to use as parent if none provided
        if parent is None:
            app = QApplication.instance()
            if app:
                for widget in app.topLevelWidgets():
                    if widget.isVisible():
                        parent = widget
                        break

        super().__init__(parent)

        self.selected_path = None
        self.args = args

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
        for i, name in enumerate(self.args):
            display_text = f"{i+1}. {name}"
            self.path_combo.addItem(display_text, name)
        layout.addWidget(self.path_combo)

        # Confirm button
        confirm_button = QPushButton("确认")
        confirm_button.clicked.connect(self.on_confirm)
        layout.addWidget(confirm_button)

        # Cancel button
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.on_cancel)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.resize(300, 150)

    def on_confirm(self):
        """Handle confirm button click."""
        index = self.path_combo.currentIndex()
        if index >= 0 and index < len(self.args):
            self.selected_path = self.args[index]
            self.evtReturn.emit(self.selected_path)
        else:
            self.evtReturn.emit(None)
        self.accept()

    def on_cancel(self):
        """Handle cancel button click."""
        self.evtReturn.emit(None)
        self.reject()

    def closeEvent(self, event):
        """Handle dialog close event."""
        if self.selected_path is None:
            self.evtReturn.emit(None)
        super().closeEvent(event)
