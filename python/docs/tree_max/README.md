# Challenge Summary

Today's challenge was to create a method for the Binary Tree class that can find
and return the maximum value.

## Whiteboard Process

[whiteboard](./tree-max.jpg)

## Approach & Efficiency

The approach I took was to use the basic structure of a pre-order search and instead of returning all the values, keep
track of a single value that changes as it traverses the tree. The efficiency on this should be O(N^2) for space, as I
use recursive functions to traverse the tree, and O(N) for time, as it will only take a certain amount of steps for each
node in the tree we are dealing with

## Solution

[code](../../data_structures/binary_tree.py) |
[tests](../../tests/code_challenges/test_tree_max.py)
