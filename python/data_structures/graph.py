class Graph:
    """
    Creates a graph that can add vertexes and edges, return a list of vertexes, return a list of vertexes connected to a given vertex, and return the total number of vertexes within it.
    """

    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []

        return vertex


    def size(self):
        return len(self.adjacency_list)


    def get_nodes(self):
        return self.adjacency_list.keys()


    def add_edge(self, vertex1, vertex2, weight=0):
        edge = Edge(vertex2, weight)
        if vertex2 not in self.adjacency_list:
            raise KeyError
        self.adjacency_list[vertex1].append(edge)


    def get_neighbors(self, vertex):
            return self.adjacency_list[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
