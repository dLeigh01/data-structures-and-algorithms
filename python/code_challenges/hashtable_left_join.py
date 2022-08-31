from data_structures.hashtable import Hashtable


def left_join(hash1, hash2):
    merger = hash1.keys()
    for index, key in enumerate(merger):
        merger[index] = [key, hash1.get(key)]
        if key in hash2.keys():
            merger[index].append(hash2.get(key))
        else:
            merger[index].append(None)

    return merger
