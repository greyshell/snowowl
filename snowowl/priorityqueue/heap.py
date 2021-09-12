#!/usr/bin/env python3

# author: greyshell

import operator
from enum import Enum

__all__ = ['Heap', 'HeapType']


class HeapType(Enum):
    MIN = 0
    MAX = 1


class Heap:
    def __init__(self, array: list, heap_type: HeapType = HeapType.MIN) -> None:
        """
        time: O(n*logn)
            - Θ(n) -> tighter upper bound
        space: O(1)
        """
        self._heap = array
        self._heap_type = heap_type
        self._length = 0

        # build heap
        current_index = (len(self._heap) - 1) // 2
        while current_index >= 0:
            self._heapify_down(current_index)
            current_index -= 1

        self._length = len(array)

    def _has_left_child(self, current_index: int) -> bool:
        """
        time: O(1)
        space: O(1)
        """
        return self._get_left_child_index(current_index) < len(self._heap)

    def _has_right_child(self, current_index: int) -> bool:
        """
        time: O(1)
        space: O(1)
        """
        return self._get_right_child_index(current_index) < len(self._heap)

    @staticmethod
    def _get_left_child_index(current_index: int) -> int:
        """
        time: O(1)
        space: O(1)
        """
        return current_index * 2 + 1

    @staticmethod
    def _get_right_child_index(current_index: int) -> int:
        """
        time: O(1)
        space: O(1)
        """
        return current_index * 2 + 2

    def _has_parent(self, current_index: int) -> bool:
        """
        time: O(1)
        space: O(1)
        """
        return current_index != 0 and self._get_parent_index(current_index) >= 0

    @staticmethod
    def _get_parent_index(current_index: int) -> int:
        """
        time: O(1)
        space: O(1)
        """
        return (current_index - 1) // 2

    def _swap(self, a: int, b: int) -> None:
        """
        time: O(1)
        space: O(1)
        """
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]

    def _compare(self, a: object, b: object) -> bool:
        """
        time: O(1)
        space: O(1)
        """
        return operator.lt(a, b) if self._heap_type == HeapType.MIN else operator.gt(a, b)

    def _heapify_down(self, current_index: int) -> None:
        """
        time: O(log(n))
        space: O(1)
        """
        while self._has_left_child(current_index):
            swappable_child_index = self._get_left_child_index(current_index)
            if self._has_right_child(current_index) and \
                    self._compare(self._heap[self._get_right_child_index(current_index)],
                                  self._heap[self._get_left_child_index(current_index)]):
                swappable_child_index = self._get_right_child_index(current_index)

            if self._compare(self._heap[current_index], self._heap[swappable_child_index]):
                break

            self._swap(current_index, swappable_child_index)
            current_index = swappable_child_index

    def _heapify_up(self, current_index: int) -> None:
        """
        time: O(log(n))
        space: O(1)
        """
        while self._has_parent(current_index) and \
                self._compare(self._heap[current_index],
                              self._heap[self._get_parent_index(current_index)]):
            parent_index = self._get_parent_index(current_index)
            self._swap(current_index, parent_index)
            current_index = parent_index

    def peek(self) -> int:
        """
        time: O(1)
        space: O(1)
        """
        if len(self._heap) == 0:
            raise IndexError("empty heap")
        return self._heap[0]

    def remove(self) -> object:
        """
        time: O(log(n))
        space: O(1)
        """
        if len(self._heap) == 0:
            raise IndexError("empty heap")
        self._swap(0, len(self._heap) - 1)
        value = self._heap.pop()
        self._heapify_down(0)
        self._length -= 1
        return value

    def insert(self, value: object) -> None:
        """
        time: O(log(n))
        space: O(1)
        """
        self._heap.append(value)
        self._heapify_up(len(self._heap) - 1)
        self._length += 1

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        return self._heap[i]

    def __str__(self):
        return str(self._heap)

