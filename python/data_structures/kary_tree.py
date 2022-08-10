from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self):
        if self.root is None:
            return KaryTree()

        queue = Queue()
        clone_queue = Queue()
        queue.enqueue(self.root)
        cloned_root = Node(self.root.value)
        clone_queue.enqueue(cloned_root)


        while queue.is_empty() is False:
            node = queue.dequeue()
            cloned_node = clone_queue.dequeue()

            for child in node.children:
                queue.enqueue(child)
                cloned_child = Node(child.value)
                clone_queue.enqueue(cloned_child)
                cloned_node.children.append(cloned_child)

        return KaryTree(cloned_root)


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
