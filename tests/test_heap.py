#!/usr/bin/env python3

# author: greyshell
# command: python -m pytest test_heap.py -v

import pytest
import operator
from snowowl import Heap, HeapType


class Node:
    """helper class"""
    def __init__(self, key, age):
        self.key = key
        self.age = age

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


def is_heap_property_satisfied(array, heap_type=HeapType.MIN):
    """helper function to test the heap property"""
    for current_idx in range(1, len(array)):
        parent_idx = (current_idx - 1) // 2
        if heap_type == HeapType.MIN:
            if operator.gt(array[parent_idx], array[current_idx]):
                return False
        elif heap_type == HeapType.MAX:
            if operator.lt(array[parent_idx], array[current_idx]):
                return False
    return True


def test_case_1() -> None:
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    min_heap = Heap(array)
    min_heap.insert(76)
    assert is_heap_property_satisfied(array) is True
    assert min_heap.peek() == -5
    assert min_heap.remove() == -5
    assert is_heap_property_satisfied(array) is True


def test_case_2():
    h1 = Node(10, 7)
    h2 = Node(5, 8)
    h3 = Node(4, 9)
    h4 = Node(2, 5)
    h5 = Node(1, 0)
    array = [h1, h2, h3, h4]
    min_heap = Heap(array)

    assert min_heap.peek() == h4
    assert is_heap_property_satisfied(array) is True

    min_heap.insert(h5)
    assert is_heap_property_satisfied(array) is True
    assert min_heap.peek() == h5
    assert min_heap.remove() == h5
    assert is_heap_property_satisfied(array) is True

    assert min_heap.peek() == h4
    assert min_heap.remove() == h4
    assert is_heap_property_satisfied(array) is True

    h6 = Node(-1, 0)
    min_heap.insert(h6)
    assert is_heap_property_satisfied(array) is True

    assert min_heap.peek() == h6
    assert min_heap.peek().key == h6.key
    assert min_heap.remove() == h6
    assert is_heap_property_satisfied(array) is True


def test_case_3():
    array = []
    min_heap = Heap(array)
    assert is_heap_property_satisfied(array) is True
    with pytest.raises(IndexError):
        assert min_heap.peek()


def test_case_4():
    array = []
    min_heap = Heap(array)
    assert is_heap_property_satisfied(array) is True
    with pytest.raises(IndexError):
        assert min_heap.remove()


def test_case_5() -> None:
    array = [5, 10, 2, 1, 20]
    max_heap = Heap(array, HeapType.MAX)
    assert is_heap_property_satisfied(array, HeapType.MAX) is True
    max_heap.insert(76)
    assert is_heap_property_satisfied(array, HeapType.MAX) is True
    assert max_heap.peek() == 76
    assert max_heap.remove() == 76
    assert is_heap_property_satisfied(array, HeapType.MAX) is True
