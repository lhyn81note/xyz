import sys
from PySide6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsLineItem
)
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QBrush

qss_string = """
NodeItem {
    background-color: rgb(50, 100, 200);
    border: 2px solid black;
    border-radius: 30px;
    color: white;
    font: 12pt "Arial";
}
NodeItem:hover {
    background-color: rgb(80, 130, 230);
    border: 2px solid red;
}
"""

NODE_CONFIG = [
    {"id": "001", "name": "HEAD", "x": 0, "y": 0},
    {"id": "002", "name": "Node 2", "x": 100, "y": 100},
    {"id": "003", "name": "Node 3", "x": 200, "y": 200},
]


class NodeItem(QGraphicsItem):
    NODE_RADIUS = 30
    CONNECTION_OFFSET = 40  # 连接线偏移量
    
    def __init__(self, node_id, name, parent=None):
        super().__init__(parent)
        self.node_id = node_id
        self.name = name
        self.parent = parent
        self.children = []
        self.hovered = False
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)  # Enable dragging
        self.setAcceptHoverEvents(True)
        self.setPos(0, 0)  # 初始位置将由布局管理器设置

    def boundingRect(self):
        return QRectF(-self.NODE_RADIUS, -self.NODE_RADIUS, 
                     self.NODE_RADIUS*2, self.NODE_RADIUS*2)

    def paint(self, painter, option, widget):
        # Apply QSS styles
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(50, 100, 200)) if not self.hovered else QBrush(QColor(80, 130, 230))
        painter.setBrush(brush)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(self.boundingRect())

        # 绘制文字
        painter.setPen(Qt.white)
        painter.setFont(QFont("Arial", 12))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.name)

        # 绘制连接标识
        if self.hovered:
            painter.setPen(Qt.red)
            painter.setBrush(Qt.red)
            # 绘制"+"号
            painter.drawLine(
                QPointF(-self.NODE_RADIUS/2, 0),
                QPointF(self.NODE_RADIUS/2, 0)
            )
            painter.drawLine(
                QPointF(0, -self.NODE_RADIUS/2),
                QPointF(0, self.NODE_RADIUS/2)
            )

    def hoverEnterEvent(self, event):
        self.hovered = True
        self.scene().update()
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.hovered = False
        self.scene().update()
        super().hoverLeaveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        # Notify the parent view to redraw connections
        if self.scene():
            self.scene().parent().redraw_connections()

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        self.scene().update()

class NodeGraphView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.nodes = {}
        self.init_nodes()
        self.setSceneRect(-400, -300, 800, 600)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def init_nodes(self):
        for node_config in NODE_CONFIG:
            node = NodeItem(node_config["id"], node_config["name"])
            node.setPos(node_config["x"], node_config["y"])
            self.nodes[node_config["id"]] = node
            self.scene.addItem(node)

        # Draw connections
        self.redraw_connections()

    def redraw_connections(self):
        # Clear existing lines
        for item in self.scene.items():
            if isinstance(item, QGraphicsLineItem):
                self.scene.removeItem(item)

        # Redraw connections
        for i in range(len(NODE_CONFIG) - 1):
            node_a = self.nodes[NODE_CONFIG[i]["id"]]
            node_b = self.nodes[NODE_CONFIG[i + 1]["id"]]
            self.scene.addLine(
                node_a.pos().x(), node_a.pos().y(),
                node_b.pos().x(), node_b.pos().y(),
                QPen(Qt.black, 2)
            )

    def update_layout(self):
        print(1, "开始布局")
        """Update the layout of the nodes and redraw connections."""
        for node_id, node in self.nodes.items():
            # Optionally, you can implement a layout algorithm here
            # For now, we just ensure the nodes are in their current positions
            node.setPos(node.pos())
        self.redraw_connections()

    def mousePressEvent(self, event):
        print(2, "鼠标按下事件")
        """处理节点连接创建"""
        # 使用新的API获取鼠标位置
        pos = event.globalPosition().toPoint()  # 获取全局坐标并转换为QPoint
        
        # 转换为视图坐标
        view_pos = self.mapFromGlobal(pos)
        
        clicked_item = self.itemAt(view_pos)  # 正确使用视图坐标
        
        if isinstance(clicked_item, NodeItem) and clicked_item.hovered:
            new_node = NodeItem(f"{len(self.nodes)+1:03d}", f"Node {len(self.nodes)+1}")
            parent = clicked_item
            new_node.setPos(parent.pos().x(), parent.pos().y() + NodeItem.CONNECTION_OFFSET)
            
            # 添加连接线
            line = self.scene.addLine(
                parent.pos().x() + NodeItem.NODE_RADIUS,
                parent.pos().y() + NodeItem.NODE_RADIUS,
                new_node.pos().x() - NodeItem.NODE_RADIUS,
                new_node.pos().y() - NodeItem.NODE_RADIUS,
                QPen(Qt.red, 2)
            )
            
            parent.add_child(new_node)
            self.nodes[new_node.node_id] = new_node
            self.update_layout()
        else:
            super().mousePressEvent(event)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    view = NodeGraphView()
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec())