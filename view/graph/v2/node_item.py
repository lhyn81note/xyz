from PySide6.QtWidgets import QGraphicsItem, QGraphicsProxyWidget
from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QPen, QFont

class NodeItem(QGraphicsItem):
    def __init__(self, node_id, label, is_end=False):
        super().__init__()
        self.node_id = node_id
        self.label = label
        self.is_end = is_end
        self.parent = None
        self.child_items = []
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)
        self.is_hovered = False

    def boundingRect(self):
        return QRectF(-60, -30, 120, 60).adjusted(-2, -2, 2, 2)

    def paint(self, painter, option, widget):
        # 绘制背景
        bg_color = QColor(179, 216, 245) if not self.is_end else QColor(155, 205, 155)
        painter.fillRect(self.boundingRect(), bg_color)
        
        # 绘制边框
        pen = QPen(QColor(67, 164, 212), 1.5)
        painter.setPen(pen)
        painter.drawRect(self.boundingRect().adjusted(0, 0, -1, -1))
        
        # 绘制文字
        painter.setPen(Qt.black)
        painter.setFont(QFont("Microsoft YaHei", 12))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.label)
        
        # 绘制+号
        if self.is_hovered:
            painter.setPen(Qt.red)
            painter.setBrush(Qt.red)
            painter.drawEllipse(QPointF(0, 25), 8, 8)
            painter.drawLine(-5, 25, 5, 25)
            painter.drawLine(0, 20, 0, 30)

    def hoverEnterEvent(self, event):
        self.is_hovered = True
        self.update()
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.is_hovered = False
        self.update()
        super().hoverLeaveEvent(event)