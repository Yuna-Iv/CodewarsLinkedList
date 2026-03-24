"""Str ll to instance ll."""
class Node:
    """Init"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """Str to ll structure."""
    list_of_values = list_repr.split(" -> ")
    head = None
    for el in reversed(list_of_values):
        if el == "None":
            continue
        head = Node(int(el), head)
    return head
