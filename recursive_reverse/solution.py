"""Recursive reverse"""
class Node(object):
    """initialization"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """recursion itself"""
    def reverse(node, prev):
        if node is None:
            return prev
        lst_rest = node.next
        node.next = prev
        return reverse(lst_rest, node)
    return reverse(head, None)
