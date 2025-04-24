import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsProxyWidget
from node_manager import NodeManager

CONFIG = {
    "head_node_id": "001",
    "001": ["002", "003"],
    "002": ["004", "005"],
    "003": ["006", "007"],
    "004": ["end"],
    "005": ["end"],
    "006": ["end"],  
    "007": ["end"]
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = NodeManager()
        self.manager.load_config(CONFIG)
        self.manager.calculate_layout()
        
        # 设置视图
        self.view = QGraphicsView(self.manager.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setSceneRect(0, 0, 800, 600)
        self.setCentralWidget(self.view)
        
        # 连接信号
        self.manager.head_node.mousePressEvent = self.on_node_click

    def on_node_click(self, event):
        """处理节点点击事件"""
        parent = self.manager.head_node
        new_node = NodeItem("NEW_NODE", "新节点")
        new_node.setPos(parent.pos().x(), parent.pos().y() + 150)
        self.manager.scene.addItem(new_node)
        parent.child_items.append(new_node)
        self.manager.calculate_layout()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())