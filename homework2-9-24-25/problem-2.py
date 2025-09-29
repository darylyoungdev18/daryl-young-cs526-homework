class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def doIt(node):
    if node is None:
        return 0
    doIt(node.next)
    print(node.value)


node4 = Node(12)
node3 = Node(3, node4)
node2 = Node(5, node3)
node1 = Node(2, node2)

doIt(node1)

""" 
the output of the code would be an output of the note values in reverse order
"""