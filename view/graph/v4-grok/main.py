import sys
import json
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl

# Parse JSON to extract head node and tree structure
def parse_json(json_str):
    data = json.loads(json_str)
    head_node_id = data.get("head_node_id")
    if not head_node_id:
        raise ValueError("JSON must contain 'head_node_id'")
    tree = {k: v if v != ["end"] else [] for k, v in data.items() if k != "head_node_id"}
    return head_node_id, tree

# Compute (x, y) positions for each node
def compute_positions(head_node, tree, canvas_width=800, canvas_height=600, node_width=100, node_height=50):
    from collections import deque
    positions = {}
    depth_counts = {}
    queue = deque([(head_node, 0)])  # (node, depth)
    while queue:
        node, depth = queue.popleft()
        if depth not in depth_counts:
            depth_counts[depth] = 0
        depth_counts[depth] += 1
        positions[node] = {"depth": depth, "index": depth_counts[depth] - 1}
        for child in tree.get(node, []):
            queue.append((child, depth + 1))
    
    max_depth = max(depth_counts.keys()) if depth_counts else 0
    for node, info in positions.items():
        depth = info["depth"]
        index = info["index"]
        nodes_at_depth = depth_counts[depth]
        x = (index + 1) * (canvas_width / (nodes_at_depth + 1)) - node_width / 2
        y = depth * (canvas_height / (max_depth + 1)) + node_height / 2
        positions[node] = {"x": x, "y": y}
    return positions

# Generate models for QML
def generate_models(head_node, tree, positions):
    nodes_model = []
    connections_model = []
    for node in tree:
        nodes_model.append({"id": node, "text": node, "x": positions[node]["x"], "y": positions[node]["y"]})
        for child in tree[node]:
            if child in positions:
                connections_model.append({"from": node, "to": child})
    return nodes_model, connections_model

# Example JSON configuration
json_str = '''
{
    "head_node_id": "开始",
    "开始": ["002", "003"],
    "002": ["004", "005"],
    "003": ["006", "007"],
    "004": ["end"],
    "005": ["end"],
    "006": ["end"],
    "007": ["end"]
}
'''

# Parse JSON
head_node, tree = parse_json(json_str)

# Compute positions
positions = compute_positions(head_node, tree)

# Generate models
nodes_model, connections_model = generate_models(head_node, tree, positions)

# Set up PySide6 application
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

# Pass data to QML
context = engine.rootContext()
context.setContextProperty("nodesData", nodes_model)
context.setContextProperty("connectionsData", connections_model)

# Load QML file
engine.load(QUrl.fromLocalFile("main.qml"))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())