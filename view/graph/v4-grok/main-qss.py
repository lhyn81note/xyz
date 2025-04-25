import sys
import json
# from PySide6.QtGui import QGuiApplication
# from PySide6.QtQml import QQmlApplicationEngine
# from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication

from view import Window

# Parse JSON to extract head node and tree structure
def parse_json(json_str):
    data = json.loads(json_str)
    head_node_id = data.get("head_node_id")
    if not head_node_id:
        raise ValueError("JSON must contain 'head_node_id'")
    tree = {k: v if v != ["end"] else [] for k, v in data.items() if k != "head_node_id"}
    print(tree)
    return head_node_id, tree

# # Set up PySide6 application
# app = QGuiApplication(sys.argv)
# engine = QQmlApplicationEngine()

# # Pass data to QML
# context = engine.rootContext()
# context.setContextProperty("nodesData", nodes_model)
# context.setContextProperty("connectionsData", connections_model)

# # Load QML file
# engine.load(QUrl.fromLocalFile("main.qml"))

# if not engine.rootObjects():
#     sys.exit(-1)

# sys.exit(app.exec())

if __name__ == '__main__':
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

    app = QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.show()
    sys.exit(app.exec())
