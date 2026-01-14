from __future__ import annotations

import time
import heapq

from collections import deque
from abc import ABC, abstractmethod
from functools import total_ordering
from typing import List, Deque, Union


class IterableMixin:
    _elements: Union[Deque, List]

    def __iter__(self):
        while self:
            yield self.dequeue()

    def __len__(self):
        return len(self._elements)

    def is_empty(self):
        return len(self) == 0

    def dequeue(self): ...


class AbstractLine(ABC, IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    @abstractmethod
    def dequeue(self): ...


class Queue(AbstractLine):
    def dequeue(self):
        return self._elements.popleft()


class Stack(AbstractLine):
    def dequeue(self):
        return self._elements.pop()


@total_ordering
class Node:
    def __init__(self, data, priority):
        self.data = data
        self._priority = (priority, time.time())

    def __eq__(self, other: Node) -> bool:
        return self._priority == other._priority

    def __lt__(self, other: Node) -> bool:
        return self._priority < other._priority

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


class PriorityQueue(IterableMixin):

    def __init__(self):
        self._elements = []

    def enqueue(self, data, priority):
        heapq.heappush(self._elements, Node(data, priority))

    def dequeue(self):
        try:
            return heapq.heappop(self._elements)
        except IndexError:
            raise


if __name__ == '__main__':
    pass
