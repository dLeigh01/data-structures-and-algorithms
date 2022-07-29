from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Creates a FILO Stack with the methods push, pop, is_empty, and peek
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        target = self.top
        self.top = self.top.next
        return target.value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
