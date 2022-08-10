class BinaryTree:
    """
    Instantiates a Binary Tree object that can search in pre order, in order, or post order
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

    def find_maximum_value(self):
        def _tree_max(node, max_value):
            if node.value > max_value:
                max_value = node.value
            if node.left:
                max_value = _tree_max(node.left, max_value)
            if node.right:
                max_value = _tree_max(node.right, max_value)
            return max_value

        if self.root is not None:
            max_value = self.root.value
            return _tree_max(self.root, max_value)
        return None


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
