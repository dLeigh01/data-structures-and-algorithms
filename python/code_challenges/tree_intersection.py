from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable
from data_structures.queue import Queue


def tree_intersection(tree1, tree2):
    checker = Hashtable()
    values = []

    breadth_hash_search(tree1, checker)
    check_hash_contains(tree2, checker, values)

    return set(values)


def check_hash_contains(tree, checker, values):
    queue = Queue()
    if tree.root is not None:
        queue.enqueue(tree.root)

    while queue.is_empty() is False:
        node = queue.dequeue()
        if checker.contains(str(node.value)):
            values.append(node.value)
        if node.right:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)


def breadth_hash_search(tree, checker):
    queue = Queue()
    if tree.root is not None:
        queue.enqueue(tree.root)

    while queue.is_empty() is False:
        node = queue.dequeue()
        checker.set(str(node.value), 1)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

