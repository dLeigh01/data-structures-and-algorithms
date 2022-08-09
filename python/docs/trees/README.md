# Trees

Binary trees are a multi-linked structure of Nodes that can be ordered or non-ordered and are searchable.

[Binary Tree Code](../../data_structures/binary_tree.py) |
[Tests](../../tests/data_structures/test_binary_tree.py) ||
[Binary Search Tree Code](../../data_structures/binary_search_tree.py) |
[Tests](../../tests/data_structures/test_binary_search_tree.py)

## Challenge

Create a Binary Tree with the ability to search pre-order, in order, and post order, as well as a Binary Search Tree
that can add a new node to the correct location and check whether said value is in the tree

## Approach & Efficiency

My approach for the two items today was to use recursive functions to move throughout the tree and either find or add
data as necessary. The space efficiency for these are O(N^2), since the more nodes there are on the tree, the more
functions will need to be added to the stack, while time will likely be O(N) as the number of steps only increases in a
linear fashion with the size of the tree.

## API

N/A
