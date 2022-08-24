import pytest
from code_challenges.quick_sort import quick_sort

def test_quick_sort_exists():
    assert quick_sort


def test_sort_empty_list():
    actual = quick_sort([], 0, 0)
    expected = []
    assert actual == expected


def test_sort_two_items():
    actual = quick_sort([5,1], 0, 1)
    expected = [1,5]
    assert actual == expected


def test_sorted_items():
    actual = quick_sort([1,2,3,4,5], 0, 4)
    expected = [1,2,3,4,5]
    assert actual == expected


def test_sort_list():
    actual = quick_sort([5,7,2,1,3], 0, 4)
    expected = [1,2,3,5,7]
    assert actual == expected


def test_repeated_numbers():
    actual = quick_sort([1,1,5,3,1,7,2,7], 0, 7)
    expected = [1,1,1,2,3,5,7,7]
    assert actual == expected
