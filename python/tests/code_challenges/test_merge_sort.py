import pytest
from code_challenges.merge_sort import merge_sort

def test_merge_sort_exists():
    assert merge_sort


def test_sort_empty_list():
    actual = merge_sort([])
    expected = []
    assert actual == expected


def test_sort_two_items():
    actual = merge_sort([5,1])
    expected = [1,5]
    assert actual == expected


def test_sorted_items():
    actual = merge_sort([1,2,3,4,5])
    expected = [1,2,3,4,5]
    assert actual == expected


def test_sort_list():
    actual = merge_sort([5,7,2,1,3])
    expected = [1,2,3,5,7]
    assert actual == expected


def test_repeated_numbers():
    actual = merge_sort([1,1,5,3,1,7,2,7])
    expected = [1,1,1,2,3,5,7,7]
    assert actual == expected
