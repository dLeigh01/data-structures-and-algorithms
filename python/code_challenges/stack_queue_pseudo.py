from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)
        self.rear = self.stack1.top
        if self.front is None:
            self.front = self.rear

    def dequeue(self):
        if self.stack1.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        while self.stack1.is_empty() is False:
            self.stack2.push(self.stack1.pop())
        value = self.stack2.pop()
        while self.stack2.is_empty() is False:
            self.stack1.push(self.stack2.pop())
        return value

    def peek(self):
        pass

    def is_empty(self):
        pass
