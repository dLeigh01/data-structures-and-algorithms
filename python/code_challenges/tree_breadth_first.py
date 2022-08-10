from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    response = []
    queue = Queue()

    if tree.root is not None:
        queue.enqueue(tree.root)

    while queue.is_empty() is False:
        node = queue.dequeue()
        response.append(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
            print(queue.front)
            print(node.right.value)

    return response
