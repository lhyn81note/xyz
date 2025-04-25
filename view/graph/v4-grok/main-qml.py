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
    print(tree)
    return head_node_id, tree

# Compute (x, y) positions for each node
def compute_positions(head_node, tree, canvas_width=800, canvas_height=600, node_width=100, node_height=50):
    """
    Calculate the (x, y) positions for each node in a tree structure for graphical representation.

    Args:
        head_node (str): The ID of the head (root) node.
        tree (dict): A dictionary representing the tree structure, where keys are node IDs and values are lists of child node IDs.
        canvas_width (int): The width of the canvas where nodes will be displayed.
        canvas_height (int): The height of the canvas where nodes will be displayed.
        node_width (int): The width of each node (used for spacing calculations).
        node_height (int): The height of each node (used for spacing calculations).

    Returns:
        dict: A dictionary where keys are node IDs and values are dictionaries containing 'x' and 'y' coordinates.
    """
    from collections import deque

    # Initialize data structures
    positions = {}  # Stores the computed positions for each node
    depth_counts = {}  # Tracks the number of nodes at each depth level
    queue = deque([(head_node, 0)])  # Queue for BFS traversal, storing (node, depth)

    # Explain BFS traversal
    # We start from the head node and explore its children, then their children, and so on.
    # This ensures that we process nodes level by level, which is useful for calculating their positions.
    # The queue will hold tuples of (node, depth) where depth is the level of the node in the tree.
    # The depth_counts dictionary will help us determine how many nodes are at each depth level,
    # which is important for calculating the x-coordinates of the nodes.
    # The BFS traversal will also help us assign a unique index to each node at its depth level,
    # which is used to calculate the x-coordinate.
    # Initialize the queue with the head node at depth 0
    # The queue will be used to perform a breadth-first search (BFS) on the tree structure.
    # The depth_counts dictionary will keep track of how many nodes are at each depth level.
    # The positions dictionary will store the computed (x, y) coordinates for each node.
    # The BFS will ensure that we process nodes level by level, which is useful for calculating their positions.
    # The depth_counts dictionary will help us determine how many nodes are at each depth level,

    # Perform BFS to assign depth and index for each node
    print(queue)

    while queue:
        node, depth = queue.popleft()
        if depth not in depth_counts:
            depth_counts[depth] = 0
        depth_counts[depth] += 1
        # Assign depth and index for the current node
        positions[node] = {"depth": depth, "index": depth_counts[depth] - 1}
        # Add child nodes to the queue
        for child in tree.get(node, []):
            queue.append((child, depth + 1))


    
    # Calculate maximum depth of the tree
    max_depth = max(depth_counts.keys()) if depth_counts else 0

    # Compute (x, y) coordinates for each node
    for node, info in positions.items():
        depth = info["depth"]
        index = info["index"]
        nodes_at_depth = depth_counts[depth]
        # Calculate x-coordinate based on the node's index at its depth
        x = (index + 1) * (canvas_width / (nodes_at_depth + 1)) - node_width / 2
        # Calculate y-coordinate based on the node's depth
        y = depth * (canvas_height / (max_depth + 1)) + node_height / 2
        # Update the position with calculated coordinates
        positions[node] = {"x": x, "y": y}

    print(queue)
    print(positions)
    print("Max depth:", max_depth)
    print("Depth counts:", depth_counts)


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
    print("Nodes model:", nodes_model)
    print("Connections model:", connections_model)
    return nodes_model, connections_model

# Example JSON configuration
json_str = '''
{
    "head_node_id": "开始",
    "开始": ["002", "003"],
    "002": ["004", "005"],
    "003": ["006", "007"],
    "004": ["end"],
    "005": ["003"],
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