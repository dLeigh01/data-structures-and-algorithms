from data_structures.graph import Graph


def direct_flights(routes, path):
    price = 0
    nodes = routes.get_nodes()


    for i in range(1, len(path)):
        neighbors = []
        for node in nodes:
            if node.value == path[i-1]:
                edges = routes.get_neighbors(node)
                break

        for edge in edges:
            neighbors.append(edge.vertex.value)
        if path[i] in neighbors:
            for edge in edges:
                if edge.vertex.value == path[i]:
                    price += edge.weight
        else:
            return tuple([False, 0])

    return tuple([True, price])
