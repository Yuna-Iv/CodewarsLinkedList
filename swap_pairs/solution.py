"""Swap node pairs"""
class Node:
    """initialise"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """swapping"""
    if head is None or head.next is None:
        return head

    dummy = Node(next=head)
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        first  = prev.next
        second = prev.next.next

        first.next  = second.next
        second.next = first
        prev.next   = second
        prev = first
    return dummy.next
