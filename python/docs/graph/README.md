# Graphs

[code](../../data_structures/graph.py) | [tests](../../tests/data_structures/test_graph.py)

A graph is similar to a tree, but the nodes are called vertexes that can be connected in any way, including back anf forth, and the lines between them are called edges, which can also have a weight.

## Challenge

Create a working graph data structure that can add nodes, tell you all the nodes it contains, tell you it's size, and create edges between nodes/ return what nodes are linked to any given node.

## Approach & Efficiency

The approach for this was to add any new vertex to the dictionary created upon instantiation, and adding connections between them using an Edge structure that is added to that vertexes value in the dictionary. Most of (if not all) the things within this should be O(1) efficiency for time and for space.
