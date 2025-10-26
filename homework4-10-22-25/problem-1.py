from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def preorder_traversal(node):
    if not node:
        return
    print(node.val, end=" ")
    for child in node.children:
        preorder_traversal(child)

def breadth_first_traversal(root):
    if not root: 
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.val, end=" ")
        for child in current.children:
            queue.append(child)

def postorder_traversal(node):
    if not node:
        return
    for child in node.children:
        postorder_traversal(child)
    print(node.val, end=" ")


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

def parse_value(val_str):
    """
    Try to parse as int first, if it fails use as string
    """
    try:
        return int(val_str)
    except ValueError:
        return val_str

def build_tree_from_input():
    """
    Build n-ary tree from standard input
    Works with both integers and strings
    Format: Each line contains: parent_value child1 child2 child3 ...
    First line is the root
    """
    try:
        nodes = {}
        root = None
        
        # Read number of nodes or lines
        n = int(input().strip())
        
        for i in range(n):
            line = input().strip().split()
            if not line:
                continue
            
            # Parse parent value (int or string)
            parent_val = parse_value(line[0])
            
            # Create parent node if doesn't exist
            if parent_val not in nodes:
                nodes[parent_val] = Node(parent_val)
            
            # First node is root
            if root is None:
                root = nodes[parent_val]
            
            # Add children
            for j in range(1, len(line)):
                child_val = parse_value(line[j])
                if child_val not in nodes:
                    nodes[child_val] = Node(child_val)
                nodes[parent_val].children.append(nodes[child_val])
        
        return root
    
    except Exception as e:
        print(f"Error parsing input: {e}")
        return None

def main():
    """
    Main function with standard input/output
    Input format:
    Line 1: Number of parent nodes
    Lines 2-n: parent_value child1 child2 child3 ...
    
    Example with integers:
    4
    1 2 3 4
    2 5 6
    3 7
    4 8 9
    
    Example with strings:
    4
    A B C D
    B E F
    C G
    D H I
    
    Example with mixed:
    3
    root left right
    left child1 child2
    right child3
    """
    print("Building tree from input...")
    root = build_tree_from_input()
    
    if not root:
        print("Failed to build tree")
        return
    
    print("\nPreorder Traversal:")
    preorder_traversal(root)
    print()
    
    print("\nBreadth-First Traversal:")
    breadth_first_traversal(root)
    print()
    
    print("\nPostorder Traversal:")
    postorder_traversal(root)
    print()

if __name__ == "__main__":
    main()