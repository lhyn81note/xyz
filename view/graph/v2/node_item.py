from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt, Signal

class NodeItem(QWidget):
    clicked = Signal(str)  # 传递节点ID
    hoverEntered = Signal(str)
    hoverExited = Signal(str)

    def __init__(self, node_id, label, is_end=False, parent=None):
        super().__init__(parent)
        self.node_id = node_id
        self.is_end = is_end
        self.setup_ui()
        self.load_stylesheet()
        self.child_items = []  # 子节点列表
        
        # 连接信号
        self.hoverEntered.connect(lambda: self.hoverEntered.emit(node_id))
        self.hoverExited.connect(lambda: self.hoverExited.emit(node_id))

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        
        self.label_widget = QLabel(self)
        self.label_widget.setAlignment(Qt.AlignCenter)
        self.label_widget.setObjectName("node-label")
        
        self.plus_button = QPushButton("+", self)
        self.plus_button.setFixedSize(16, 16)
        self.plus_button.hide()
        
        layout.addWidget(self.label_widget)
        layout.addWidget(self.plus_button)

    def load_stylesheet(self):
        """加载QSS样式表"""
        self.setStyleSheet(open("node_style.qss").read())
        self.update_style()

    def update_style(self):
        """根据状态更新样式"""
        if self.is_end:
            self.setProperty("isEnd", True)
        else:
            self.setProperty("isEnd", False)
        self.style().polish(self)

    def enterEvent(self, event):
        self.plus_button.show()
        self.hoverEntered.emit(self.node_id)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.plus_button.hide()
        self.hoverExited.emit(self.node_id)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.clicked.emit(self.node_id)
        super().mousePressEvent(event)