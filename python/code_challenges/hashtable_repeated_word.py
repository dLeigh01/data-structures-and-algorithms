from data_structures.hashtable import Hashtable
import string


def first_repeated_word(text):
    hash = Hashtable()
    stripped_words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    for word in stripped_words:
        if hash.contains(word):
            return word
        hash.set(word, 1)
