from data_structures.queue import Queue
from data_structures.stack import Stack


class AnimalShelter:
    def __init__(self):
        self.animals = Stack()
        self.sorting = Queue()

    def enqueue(self, value):
        self.animals.push(value)

    def dequeue(self, pref):
        target = None
        while self.animals.top:
            current_critter = self.animals.pop()
            if current_critter.type == pref:
                target = current_critter
            self.sorting.enqueue(current_critter)

        while self.sorting.front:
            current_critter = self.sorting.dequeue()
            if current_critter == target:
                continue
            self.animals.push(current_critter)
            previous = current_critter
        return target


class Dog:
    def __init__(self):
        self.type = "dog"


class Cat:
    def __init__(self):
        self.type = "cat"
