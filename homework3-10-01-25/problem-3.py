class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_array_recursive(arr):
    """Recursively reverse an array"""
    if len(arr) <= 1:
        return arr
    return reverse_array_recursive(arr[1:]) + [arr[0]]

def reverse_linked_list_recursive(head):
    """Recursively reverse a linked list"""
    if not head or not head.next:
        return head
    
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse_doubly_linked_list_recursive(head):
    """Recursively reverse a doubly linked list"""
    if not head:
        return None
    
    head.next, head.prev = head.prev, head.next
    
    if not head.prev:
        return head
    
    return reverse_doubly_linked_list_recursive(head.prev)


def create_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for item in data[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def create_doubly_linked_list(data):
    if not data:
        return None
    head = DoublyListNode(data[0])
    current = head
    for item in data[1:]:
        new_node = DoublyListNode(item)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def display_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def main():
    # Read input from standard input
    try:
        input_line = input().strip()
        test_data = [int(x.strip()) for x in input_line.split(',')]
    except:
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Test Array (simple list)
    print("Array reversal:")
    print("Input: ", test_data)
    reversed_array = reverse_array_recursive(test_data.copy())
    print("Output:", reversed_array)
    print()
    
    # Test Linked List
    print("Linked List reversal:")
    linked_list = create_linked_list(test_data)
    print("Input: ", display_linked_list(linked_list))
    reversed_linked = reverse_linked_list_recursive(linked_list)
    print("Output:", display_linked_list(reversed_linked))
    print()
    
    # Test Doubly Linked List
    print("Doubly Linked List reversal:")
    doubly_list = create_doubly_linked_list(test_data)
    print("Input: ", display_linked_list(doubly_list))
    reversed_doubly = reverse_doubly_linked_list_recursive(doubly_list)
    print("Output:", display_linked_list(reversed_doubly))

if __name__ == "__main__":
    main()