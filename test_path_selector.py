import sys
import json
import os
from PySide6.QtWidgets import QApplication
from libs.path_selector import PathSelectorDialog

# Create a sample flow JSON for testing
def create_test_flow():
    flow_data = {
        "meta": {
            "name": "Test Flow",
            "description": "A test flow for path selection"
        },
        "flow": {
            "head_node_id": "cmd1",
            "cmd1": ["cmd2", "cmd3", "cmd4"],
            "cmd2": ["cmd5"],
            "cmd3": ["cmd5"],
            "cmd4": ["cmd5"],
            "cmd5": []
        },
        "cmds": {
            "cmd1": {
                "type": "sys",
                "name": "Start Command",
                "param": {}
            },
            "cmd2": {
                "type": "sys",
                "name": "Path A",
                "param": {}
            },
            "cmd3": {
                "type": "sys",
                "name": "Path B",
                "param": {}
            },
            "cmd4": {
                "type": "sys",
                "name": "Path C",
                "param": {}
            },
            "cmd5": {
                "type": "sys",
                "name": "End Command",
                "param": {}
            }
        },
        "nodes": {
            "cmd1": {"x": 100, "y": 100},
            "cmd2": {"x": 200, "y": 50},
            "cmd3": {"x": 200, "y": 100},
            "cmd4": {"x": 200, "y": 150},
            "cmd5": {"x": 300, "y": 100}
        }
    }
    
    # Save the test flow to a file
    test_flow_path = "runtime/flows/test_path_selection.json"
    os.makedirs(os.path.dirname(test_flow_path), exist_ok=True)
    
    with open(test_flow_path, 'w') as f:
        json.dump(flow_data, f, indent=4)
    
    return test_flow_path

def test_dialog():
    # Create a QApplication instance
    app = QApplication(sys.argv)
    
    # Sample paths and command names
    paths = ["cmd2", "cmd3", "cmd4"]
    cmd_names = {
        "cmd2": "Path A",
        "cmd3": "Path B",
        "cmd4": "Path C"
    }
    
    # Create and show the dialog
    dialog = PathSelectorDialog(paths, cmd_names)
    
    if dialog.exec():
        selected_path = dialog.get_selected_path()
        print(f"Selected path: {selected_path}")
    else:
        print("Dialog canceled")

if __name__ == "__main__":
    # Test the dialog directly
    test_dialog()
    
    # Create a test flow file
    flow_path = create_test_flow()
    print(f"Created test flow at: {flow_path}")
    print("You can now test the path selection in the actual flow by running:")
    print(f"python app.py with the flow file: {flow_path}")
