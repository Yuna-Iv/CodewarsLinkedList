"""Create node"""
class Node:
    """initialization."""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """creates ll"""
    next = head
    head = Node(data)
    head.next = next
    return head

def build_one_two_three():
    """creates ll of length 3"""
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
