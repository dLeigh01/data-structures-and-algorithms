# Stacks and Queues

Stacks and Queues are data structures similar to linked lists in that each node only knows the position of one other
node, except the purpose of these is more to have a specific order that nodes enter and leave, in LILO or FILO order.

[stack code](../../data_structures/stack.py) |
[stack tests](../../tests/data_structures/test_stack.py) |||
[queue code](../../data_structures/queue.py) |
[queue tests](../../tests/data_structures/test_queue.py) |

## Challenge

Create classes for Queues and Lists that have the ability to add and remove data with O(1) methods, as well as check the
data at the front or top of the structures and check if they're empty.

## Approach & Efficiency

The approach used for today's challenge was relatively simple. The way that pop and dequeue work are both very similar,
in that it is just removing one Node from the edge of the data structure and pointing the correct variable to the new
edge in an O(1) method, but enqueuing was a bit more complex than pushing, as there are two separate variables that
exist in a queue as opposed to the singular top in a stack. Push is O(1), as the height of the stack and the value being
added have no bearing on how long it takes to complete, and I believe enqueue is also O(1), as it does have one possible
extra step based on whether the list is empty or not, but that doesn't have any sort of relationship to the amount of
data involved otherwise. The other shared methods are also both O(1), as they are only checking the outermost value in
the data structure.

## API

Both of the classes created today use [InvalidOperationError](../../data_structures/invalid_operation_error.py), which
raises an exception if they attempt to peek or remove something from an empty data structure. Both classes also bring in
the previously created [Node](../../data_structures/linked_list.py) class to use in their data structure.
