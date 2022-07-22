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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError:
    pass
