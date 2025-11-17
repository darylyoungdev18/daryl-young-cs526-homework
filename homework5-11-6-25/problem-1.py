"""
Implement a binary search tree 
Create an ADT for a Node
Create an ADT for a BST with the following functions:
Add Node(Value)
Delete Node(Value)
FindNode(Value)
PrintTree()

Demonstrate you code by randomly generating an input set of size 5 to 50 for numbers between 1 and 1000
You must print out your input set, your initial tree and then exercise your methods add and delete printing your tree after every method invocation. You must also exercise your findNode method by randomly generating a number between 1 and 1000 and printing whether or not you found the node, you must have both positive and negative cases.
You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code.


"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._addNodeRec(self.root, value)

    def _addNodeRec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._addNodeRec(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._addNodeRec(node.right, value)

    def deleteNode(self, value):
        self.root = self._deleteNodeRec(self.root, value)

    def _deleteNodeRec(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._deleteNodeRec(node.left, value)
        elif value > node.value:
            node.right = self._deleteNodeRec(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._findMin(node.right)
            node.value = min_larger_node.value
            node.right = self._deleteNodeRec(node.right, min_larger_node.value)
        return node

    def _findMin(self, node):
        while node.left:
            node = node.left
        return node

    def findNode(self, value):
        return self._findNodeRec(self.root, value)

    def _findNodeRec(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._findNodeRec(node.left, value)
        else:
            return self._findNodeRec(node.right, value)

    def printTree(self):
        self._printTreeRec(self.root)

    def _printTreeRec(self, node):
        if node:
            self._printTreeRec(node.left)
            print(node.value)
            self._printTreeRec(node.right)

if __name__ == "__main__":
    import random
    import sys

    bst = BST()

    # If a filename is provided as the first command-line argument, read that file.
    # Otherwise prompt on the console to choose file, manual entry, or random generation.
    input_values = None
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        with open(input_file_path, "r") as f:
            input_values = list(map(int, f.read().strip().split()))
    else:
        choice = input("Load from (f)ile, enter (m)anual values, or (r)andom? [f/m/r]: ").strip().lower()
        if choice == "f":
            input_file_path = input("Enter input file path: ").strip()
            with open(input_file_path, "r") as f:
                input_values = list(map(int, f.read().strip().split()))
        elif choice == "m":
            line = input("Enter numbers separated by spaces: ").strip()
            input_values = list(map(int, line.split())) if line else []
        else:
            size_str = input("Enter size (5-50) or press Enter for random size: ").strip()
            if size_str:
                size = max(5, min(50, int(size_str)))
            else:
                size = random.randint(5, 50)
            input_values = random.sample(range(1, 1001), size)

    print("Input Set:", input_values)

    for value in input_values:
        bst.addNode(value)

    print("\nInitial Tree:")
    bst.printTree()

    # Test addNode
    new_value = random.randint(1, 1000)
    print(f"\nAdding Node: {new_value}")
    bst.addNode(new_value)
    bst.printTree()

    # Test deleteNode (choose a value from the original input set if available)
    if input_values:
        del_value = random.choice(input_values)
        print(f"\nDeleting Node: {del_value}")
        bst.deleteNode(del_value)
        bst.printTree()

    # Test findNode: one positive (from input_set if available) and one negative
    if input_values:
        find_positive = random.choice(input_values)
        print(f"\nFinding Node (should be found): {find_positive} - {'Found' if bst.findNode(find_positive) else 'Not Found'}")
    find_negative = random.randint(1001, 2000)
    print(f"Finding Node (should NOT be found): {find_negative} - {'Found' if bst.findNode(find_negative) else 'Not Found'}")