from data_structures.queue import Queue

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
        return list(self.adjacency_list.keys())


    def add_edge(self, vertex1, vertex2, weight=0):
        edge = Edge(vertex2, weight)
        if vertex2 not in self.adjacency_list:
            raise KeyError
        self.adjacency_list[vertex1].append(edge)


    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


    def breadth_first(self, root):
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(root)
        visited.add(root)

        while breadth.is_empty() is False:
            current = breadth.dequeue()
            nodes.append(current.value)

            for neighbor in self.get_neighbors(current):
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)

        return nodes


    def depth_first_search(self, root):
        nodes = []
        if root not in self.get_nodes():
            return []

        def _search(node):
            nodes.append(node)
            edges = self.get_neighbors(node)
            for edge in edges:
                if edge.vertex in nodes:
                    continue
                _search(edge.vertex)

        _search(root)
        for i, node in enumerate(nodes):
            nodes[i] = node.value

        return nodes



class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
