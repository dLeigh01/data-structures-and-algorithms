from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(source):
    tree = source.clone()
    queue = Queue()
    queue.enqueue(tree.root)

    while queue.is_empty() is False:
        node = queue.dequeue()
        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = f"{node.value}"

        for child in node.children:
            queue.enqueue(child)

    return tree
