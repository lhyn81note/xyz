import json

def parse_json(json_str):
    """
    Parse the JSON string to extract the head node and the tree structure.
    
    :param json_str: JSON string representing the node configuration.
    :return: Tuple containing the head node ID and the tree dictionary.
    """
    data = json.loads(json_str)
    
    # Extract the head node ID
    head_node_id = data.get("head_node_id")
    if not head_node_id:
        raise ValueError("JSON must contain 'head_node_id'")
    
    # Build the tree structure
    tree = {}
    for key, value in data.items():
        if key != "head_node_id":
            # Replace "end" with an empty list
            if value == ["end"]:
                tree[key] = []
            else:
                tree[key] = value
    
    return head_node_id, tree

# Example usage
json_str = '''
{
    "head_node_id": "001",
    "001": ["002", "003"],
    "002": ["004", "005"],
    "003": ["006", "007"],
    "004": ["end"],
    "005": ["end"],
    "006": ["end"],
    "007": ["end"]
}
'''

head_node, tree = parse_json(json_str)
print("Head Node:", head_node)
print("Tree Structure:", tree)