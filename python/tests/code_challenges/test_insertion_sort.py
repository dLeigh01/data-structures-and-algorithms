import pytest
from code_challenges.insertion_sort import insertion_sort

def test_insertion_sort_exists():
    assert insertion_sort


def test_sort_empty_list():
    actual = insertion_sort([])
    expected = []
    assert actual == expected


def test_sort_two_items():
    actual = insertion_sort([2,1])
    expected = [1,2]
    assert actual == expected


def test_sorted_items():
    actual = insertion_sort([1,2,3,4])
    expected = [1,2,3,4]
    assert actual == expected


def test_sort_list():
    actual = insertion_sort([2,5,3,8,7,9])
    expected = [2,3,5,7,8,9]
    assert actual == expected
