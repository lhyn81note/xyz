import sys
import json
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QPainter, QPen, QColor, QFont

# 更新后的节点配置数据
CONFIG = {
    "head_node_id": "001",
    "001": ["002", "003"],
    "002": ["004", "005"],
    "003": ["006", "007"],
    "004": ["003","005"],
    "005": ["end"],
    "006": ["end"],  
    "007": ["end"]
}

class Node:
    def __init__(self, node_id, name, position):
        self.id = node_id          # 节点唯一标识
        self.name = name           # 显示名称
        self.position = position   # 节点中心位置 (QPointF)
        self.children = []         # 子节点列表
        self.is_end = False        # 是否是结束节点
        self.parent = None         # 父节点引用

class NodeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.head_node = None
        self.end_node = None
        self.init_data()
        self.calculate_layout()

    def init_data(self):
        """根据新配置数据初始化节点结构"""
        # 创建所有常规节点
        for node_id in CONFIG:
            if node_id == "head_node_id":
                continue
                
            is_end = node_id == "end"
            node_name = f"节点{node_id[-1]}" if not is_end else "结束节点"
            
            self.nodes[node_id] = Node(
                node_id,
                node_name,
                QPointF(0, 0)
            )
            self.nodes[node_id].is_end = is_end

        # 建立连接关系
        for parent_id, children_ids in CONFIG.items():
            if parent_id == "head_node_id":
                continue
                
            parent_node = self.nodes[parent_id]
            for child_id in children_ids:
                if child_id == "end":
                    # 创建统一的结束节点（如果不存在）
                    if not self.end_node:
                        self.end_node = Node(
                            "END_NODE",
                            "结束节点",
                            QPointF(self.width()/2, self.height()-50)
                        )
                        self.nodes["END_NODE"] = self.end_node
                    parent_node.children.append(self.end_node)
                    self.end_node.parent = parent_node
                else:
                    child_node = self.nodes[child_id]
                    parent_node.children.append(child_node)
                    child_node.parent = parent_node

        # 设置头节点
        self.head_node = self.nodes[CONFIG["head_node_id"]]

    def calculate_layout(self):
        """自动计算节点布局"""
        x_spacing = 200  # 水平间距
        y_spacing = 150  # 垂直间距
        
        # 计算头节点位置
        self.head_node.position = QPointF(self.width()/2, 50)
        
        # 递归计算子节点位置
        def layout_children(node, level):
            if level > 3: return  # 限制最大深度
            
            y = node.position.y() + y_spacing
            x_step = x_spacing / (len(node.children) + 1)
            
            for i, child in enumerate(node.children):
                if child.is_end:
                    continue  # 结束节点单独处理
                
                x = node.position.x() + x_step * (i + 1)
                child.position = QPointF(x, y)
                layout_children(child, level + 1)

        layout_children(self.head_node, 1)

        # 固定结束节点位置
        if self.end_node:
            self.end_node.position = QPointF(self.width()/2, self.height()-50)

    def paintEvent(self, event):
        """绘制所有元素"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制连接线（先画线后画节点）
        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        for node in self.nodes.values():
            if node.is_end:
                continue  # 跳过结束节点的出线
                
            for child in node.children:
                if child.is_end:
                    # 特殊处理指向结束节点的连线
                    painter.drawLine(
                        node.position + QPointF(50, 30),
                        self.end_node.position - QPointF(50, 30)
                    )
                else:
                    painter.drawLine(
                        node.position + QPointF(50, 30),
                        child.position - QPointF(50, 30)
                    )

        # 绘制节点
        for node in self.nodes.values():
            rect = QRectF(node.position.x() - 50, 
                         node.position.y() - 30, 
                         100, 60)
            
            # 设置节点颜色
            if node.is_end:
                color = QColor(0, 255, 0)  # 结束节点绿色
            else:
                color = QColor(200, 200, 200)  # 普通节点灰色
                
            painter.setBrush(color)
            painter.drawRect(rect)
            
            # 绘制文字
            painter.setPen(Qt.black)
            painter.setFont(QFont("Arial", 12))
            painter.drawText(rect, Qt.AlignCenter, node.name)

        # 绘制结束标记
        if self.end_node:
            end_pen = QPen(Qt.blue, 3)
            painter.setPen(end_pen)
            painter.drawLine(
                self.end_node.position.x() - 15, 
                self.end_node.position.y() + 30,
                self.end_node.position.x() + 15, 
                self.end_node.position.y() + 30
            )
            painter.drawLine(
                self.end_node.position.x() - 15, 
                self.end_node.position.y() + 35,
                self.end_node.position.x() + 15, 
                self.end_node.position.y() + 35
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NodeWidget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())