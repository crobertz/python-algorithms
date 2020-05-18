class Graph:
    """Class of (directed) graphs"""
    # takes an iterable of nodes
    def __init__(self, nodes):
        # set of nodes
        self.nodes = set(node for node in nodes)
        # shows graph as a dict of node: adjacent nodes
        self.adj = {node: set() for node in self.nodes}
        # set of tuples (source,target)
        self.edges = set(tuple([node, nbr]) for node in self.nodes for nbr in self.adj[node])
    
    def add_node(self, node):
        # add a node to graph
        self.nodes.add(node)
        if not node in self.adj:
            self.adj[node] = set()
    
    def add_edge(self, source, target):
        # add an edge to graph
        self.add_node(source)
        self.add_node(target)
        self.adj[source].add(target)
        self.edges.add(tuple([source,target]))