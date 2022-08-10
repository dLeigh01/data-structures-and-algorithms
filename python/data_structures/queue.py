from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Class creates a LILO Queue data structure with the methods enqueue, dequeue, peek, and is_empty
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if not self.rear:
            self.rear = Node(value)
            self.front = self.rear
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        target = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return target.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return self.front is None
