class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def _pre_order(node):
            arr.append(node.value)
            if node.left is not None:
                _pre_order(node.left)
            if node.right is not None:
                _pre_order(node.right)

        arr = []
        if self.root is not None:
            _pre_order(self.root)

        return arr

    def in_order(self):
        def _in_order(node):
            if node.left is not None:
                _in_order(node.left)
            arr.append(node.value)
            if node.right is not None:
                _in_order(node.right)

        arr = []
        if self.root is not None:
            _in_order(self.root)

        return arr

    def post_order(self):
        def _post_order(node):
            if node.left is not None:
                _post_order(node.left)
            if node.right is not None:
                _post_order(node.right)
            arr.append(node.value)

        arr = []
        if self.root is not None:
            _post_order(self.root)

        return arr


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
