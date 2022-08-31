import pytest
from code_challenges.hashtable_left_join import left_join
from data_structures.hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_join_synonyms_antonyms():
    synonyms = Hashtable()
    antonyms = Hashtable()

    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    expected = [
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
