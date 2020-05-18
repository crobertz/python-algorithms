class Graph:
    """Class of (directed) graphs"""
    # takes an iterable of nodes
    def __init__(self, nodes):
        # set of nodes
        self.nodes = set(node for node in nodes)
        # shows graph as a dict of node: adjacent nodes
        self.graph = {node: set() for node in self.nodes}
        # set of tuples (origin,target)
        self.edges = set(tuple([node, nbr]) for node in self.nodes for nbr in self.graph[node])