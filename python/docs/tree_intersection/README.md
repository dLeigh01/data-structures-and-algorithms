# Challenge Summary

Create a function that takes in two binary trees and returns a set of all common values between them.

## Whiteboard Process

![whiteboard](./tree-intersection.jpg)

## Approach & Efficiency

For this challenge I used a breadth first search to add all the values in the first list to a hastable, then I used a second breadth first search to check each value in the second tree against the hashtable and if any were the same I appended it to a list, then returned the list as a set at the end. The complexity for this is O(N) because I have to create a queue a couple of times for the the search functionality, as well as a hashtable, and need to run all the way through each list. This means that the time and space requirements will go up in a linear fashion with every extra node in the original lists

## Solution

[code](../../code_challenges/tree_intersection.py) |
[tests](../../tests/code_challenges/test_tree_intersection.py)
