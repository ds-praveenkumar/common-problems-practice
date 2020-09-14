# graph.py



class Node:
    """
        This class implements Node
    """
    def __init__(self, name="root"):
        self.name = name
        print(f"{self.name}")

    def __repr__(self):
        return f"{self.name}"

    def get_node(self):
        return self.name

class Graph:
    """
        This class implements Graph
    """
    def __init__(self, graph_name="default"):
        self.name = graph_name
        self.graph = {}
        self.node = []
        self.src = None
        self.dest = None
    
    def __repr__(self):
        print(f"Graph:{self.name}")
        for key, val in self.graph.items():
            print(f"{key} --> {val}")
        return "" 

    def add_vertex(self, vertex = Node):
        if  vertex in self.graph : #check if vertex is already in the graph vertex
            print ("vertex a is ready in graph")
        else:
            self.graph[vertex] = []
            print(f"vertex added: {vertex.name}")

    def add_edge(self, src=Node, dest=Node):
        self.src, self.dest = src, dest
        if self.src == self.dest: # check if source and destination is equal
            return print(f"source is equal to destination")

        if self.dest in self.graph[self.src]: # check if edge already present
            print("edge alredy present")
        else:
            self.graph[self.src].append(self.dest) # add new node
    
    def get_values(self, root=Node):
        for key, vals in self.graph.items():
            if key == root:
                return vals

    def get_keys(self):
            return self.graph.keys()



if __name__ == "__main__":
    root = Node("root")
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
