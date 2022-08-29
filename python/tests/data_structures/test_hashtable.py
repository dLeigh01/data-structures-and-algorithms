import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable


def test_table_size():
    table = Hashtable()
    actual = len(table.buckets)
    expected = 1024
    assert actual == expected


def test_set_key_value():
    table = Hashtable()
    table.set('pair', 'one')
    actual = table.contains('pair')
    expected = True
    assert actual == expected


def test_contains_false():
    table = Hashtable()
    table.set('pair', 'one')
    actual = table.contains('something')
    expected = False
    assert actual == expected


def test_get_keys_List():
    table = Hashtable()
    table.set('pair', 'one')
    table.set('second', 'pair')
    actual = table.keys()
    expected = ['pair', 'second']
    assert sorted(actual) == sorted(expected)


def test_get_by_key():
    table = Hashtable()
    table.set('pair', 'one')
    actual = table.get('pair')
    expected = 'one'
    assert actual == expected


def test_get_returns_none():
    table = Hashtable()
    table.set('pair', 'one')
    actual = table.get('something')
    expected = None
    assert actual == expected


def test_handle_collision():
    table = Hashtable()
    table.set('pair', 'one')
    table.set('pair', 'two')


def test_get_from_collision():
    table = Hashtable()
    table.set('different', 'pair')
    table.set('pair', 'one')
    table.set('pair', 'two')
    actual = table.get('pair')
    expected = ('one', 'two')
    assert sorted(actual) == sorted(expected)


def test_get_from_collision_different():
    table = Hashtable()
    table.set('pal', 'friend')
    table.set('lap', 'legs')
    assert table.get('pal') == 'friend'
    assert table.get('lap') == 'legs'


def test_hash_in_range():
    table = Hashtable(size=2)
    keys = ['these', 'are', 'all', 'keys']
    for key in keys:
        index = table.hash(key)
        assert 0 <= index <= 1
