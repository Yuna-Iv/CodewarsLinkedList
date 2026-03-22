"""Writes linked list as a string."""
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def stringify(node:list) -> str:
        """Returns a string representation of the list."""
        result_str = ""
        current_node = []

        if node is None:
            return 'None'

        while node is not None:
            current_node.append(str(node.data))
            node = node.next

        result_str = " -> ".join(current_node)
        result_str += " -> None"
        return result_str
