# dfs.py

# implement dfs algorithm
from graph import Graph, Node

class DepthFirstSearch:
    """
        This class implements Dfs
    """
    def __init__(self, root, graph):
        self.source = root
        self.graph = graph
        self.queue = []
        self.visited = []

    def traverse(self, src): 
        self.queue = self.graph.get_values(src)
        print(f"{src.name} has edges to {self.queue}")
    
    def dfs(self):
        vertices =  self.graph.get_keys()
        self.visited.append(self.source)
        for v in vertices:
            if v not in self.visited:
                self.traverse(v)
            self.visited.append(v)

if __name__ == "__main__":
    a = Node("a")
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    g = Graph('initial')
    g.add_vertex(a)
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.add_vertex(e)
    g.add_edge(b, a)
    g.add_edge(a, b)
    g.add_edge(a, d)
    g.add_edge(a, c)
    g.add_edge(d, e)
    g.add_edge(c, a)
    g.add_edge(c, d)
    print(g)
    dfs = DepthFirstSearch(a, g)
    dfs.traverse(a)
    dfs.dfs()