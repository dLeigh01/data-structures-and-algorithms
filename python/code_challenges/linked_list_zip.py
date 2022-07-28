from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    current_a = a.head
    current_b = b.head
    switch = False
    zipped = LinkedList()
    if current_a:
        zipped.insert(current_a.value)
        current_a = current_a.next
    elif current_b:
        zipped.insert(current_b.value)
        current_b = current_b.next

    current = zipped.head

    while current_b is not None or current_a is not None:
        if switch is False and current_b is not None:
            zipped.insert_after(current.value, current_b.value)
            current_b = current_b.next
            current = current.next

        if switch is True and current_a is not None:
            zipped.insert_after(current.value, current_a.value)
            current_a = current_a.next
            current = current.next

        if switch is False:
            switch = True
        else:
            switch = False

    return zipped
