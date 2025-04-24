from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import QPointF
from node_item import NodeItem

class NodeManager:
    def __init__(self):
        self.nodes = {}
        self.scene = QGraphicsScene()
        self.head_node = None
        self.end_node = None

    def load_config(self, config):
        # 创建常规节点
        for node_id in config:
            if node_id in ["head_node_id"]:
                continue
                
            # is_end = ("end" in config[node_id])
            self.nodes[node_id] = NodeItem(
                node_id,
                f"节点{node_id}",
                is_end=False
            )
        
        # 创建头节点
        self.head_node = NodeItem(
            config["head_node_id"],
            "头节点",
            is_end=False
        )
        
        # 创建结束节点
        self.end_node = NodeItem(
            "END_NODE",
            "结束节点",
            is_end=True
        )
        self.nodes["END_NODE"] = self.end_node
        
        # 建立连接关系
        for parent_id, children in config.items():
            if parent_id in ["head_node_id", "end_node_ids"]:
                continue
                
            parent = self.nodes[parent_id]
            for child_id in children:
                child = self.nodes.get(child_id, self.end_node)
                parent.child_items.append(child)
                child.parent = parent
        
        self.head_node = self.nodes[config["head_node_id"]]
        self.scene.addItem(self.head_node)

    def calculate_layout(self):
        # print(1, "开始布局")
        """自动计算节点布局"""
        x_spacing = 300
        y_spacing = 200
        
        # 布局头节点
        self.head_node.setPos(100, 100)
        self.scene.addItem(self.head_node)
        
        # 递归布局子节点
        def layout_children(node, level):
            if level > 3: return
            
            y = node.pos().y() + y_spacing
            x_step = x_spacing / (len(node.child_items) + 1)
            
            for i, child in enumerate(node.child_items):
                if child.is_end:
                    continue
                
                x = node.pos().x() + x_step * (i + 1)
                child.setPos(x, y)
                self.scene.addItem(child)
                layout_children(child, level + 1)
        
        layout_children(self.head_node, 1)
        
        # 布局结束节点
        if self.end_node:
            self.end_node.setPos(400, 500)
            self.scene.addItem(self.end_node)