from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Creates a Binary Search Tree object extending Binary Tree that can also add and
    detect the values of nodes.
    """

    def add(self, value):
        def _add(value, node):
            if value < node.value:
                if node.left:
                    _add(value, node.left)
                    return
                node.left = Node(value)
                return
            if value > node.value:
                if node.right:
                    _add(value, node.right)
                    return
                node.right = Node(value)
                return

        if self.root is None:
            self.root = Node(value)
            return
        _add(value, self.root)

    def contains(self, value):
        def _contains(value, node):
            if value == node.value:
                return True
            if value < node.value:
                if node.left:
                    return _contains(value, node.left)
                return False
            if value > node.value:
                if node.right:
                    return _contains(value, node.right)
                return False
            return False

        return _contains(value, self.root)
