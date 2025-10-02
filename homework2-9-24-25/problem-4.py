#Write a function to find the sum of the three middle nodes in a doubly linked list
#of sorted integers. You may assume the the list has an odd length.
#Ex. 2,4,8,10,15,29,41 → 33

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def find_middle_recursive(slow, fast):
    """
    Recursive helper to find the middle node using slow/fast pointers.
    - slow moves one step each call.
    - fast moves two steps each call.
    - When fast reaches end, slow is at the middle.
    """
    if fast is None or fast.next is None:
        return slow
    return find_middle_recursive(slow.next, fast.next.next)


def sum_three_middle_nodes(head):
   
    # Find the middle node recursively
    middle = find_middle_recursive(head, head)

    # Get neighbors (doubly linked list ensures we can go backwards too)
    left = middle.prev
    right = middle.next

    # Return sum of the three
    return left.val + middle.val + right.val
  


def build_doubly_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        node = ListNode(val)
        curr.next = node
        node.prev = curr
        curr = node
    return head
if __name__ == "__main__":
    import sys
    # Read integers from stdin
    values = list(map(int, sys.stdin.read().strip().split()))
    
    # Build the doubly linked list
    head = build_doubly_linked_list(values)
    
    # Compute and print the result
    print(sum_three_middle_nodes(head))
