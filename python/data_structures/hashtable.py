from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Creates a class made up of a list of linked lists of key-value pairs
    """

    def __init__(self, size=1024):
        # initialization here
        self.buckets = [None] * size
        self.size = size


    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        key_value_pair = (key, value)
        bucket.insert(key_value_pair)


    def get(self, key):
        values = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    if key == current.value[0]:
                        values.append(current.value[1])
                    current = current.next

        if len(values) >= 1:
            return tuple(values)
        return None


    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False

        current = bucket.head
        while current:
            key_value_pair = current.value
            if key_value_pair[0] == key:
                return True
            current = current.next

        return False


    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    keys_list.append(current.value[0])
                    current = current.next

        return keys_list


    def hash(self, key):
        ascii_sum = sum([ord(char) for char in key])
        index = (ascii_sum * 599) % self.size
        return index
