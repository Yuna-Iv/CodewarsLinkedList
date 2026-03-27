"""Alternating split"""
class Node(object):
    """initialization"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """init"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """implemented function"""
    if head is None or head.next is None:
        raise Exception

    first  = head
    second = head.next

    current = head
    while current is not None and current.next is not None:
        odd  = current
        even = current.next

        odd.next = even.next

        if even.next is not None:
            even.next = even.next.next
        else:
            even.next = None

        current = odd.next

    return Context(first, second)
