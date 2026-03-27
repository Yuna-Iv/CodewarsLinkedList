"""get n-th node"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """get the node of given index"""
    if index < 0:
        raise Exception
    probe = node
    count = 0
    while probe:
        if count == index:
            return probe
        count += 1
        probe = probe.next
    raise Exception
