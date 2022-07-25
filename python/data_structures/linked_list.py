class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        text = ""
        current = self.head

        while current:
            text += f"{{ {current.value} }} -> "
            current = current.next

        return text + "NULL"

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, target):
        current = self.head

        while current:
            if current.value == target:
                return True
            current = current.next

        return False

    def append(self, value):
        current = self.head

        if current is None:
            self.head = Node(value)
        else:
            while current.next:
                current = current.next

        current.next = Node(value)

    def insert_before(self, target, value):
        previous = None
        current = self.head


        while current:
            if current.value == target:
                if previous:
                    previous.next = Node(value, current)
                else:
                    self.head = Node(value, current)
                return
            previous = current
            current = current.next

        raise TargetError

    def insert_after(self, target, value):
        current = self.head

        while current:
            if current.value == target:
                current.next = Node(value, current.next)
                return
            current = current.next

        raise TargetError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError(Exception):
    pass
