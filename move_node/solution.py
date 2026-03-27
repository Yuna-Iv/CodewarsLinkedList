class Node(object):
    """initialization."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """init"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """moves first node"""
    if source is None:
        raise Exception
    node = source
    source = source.next
    node.next = dest
    dest = node
    return Context(source, dest)
