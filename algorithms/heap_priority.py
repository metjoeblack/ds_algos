

import operator
import heapq
from collections import namedtuple


class Heap:

    def __init__(self, elements=None, element_priority=lambda x: x) -> None:
        self._priority = element_priority
        if elements is not None and len(elements) > 1:
            self._heapify(elements)
        else:
            self._elements = []
    
    def __repr__(self) -> str:
        return f",\n".join(str(i) for i in self._elements)
    
    def __len__(self):
        return len(self._elements)
    
    def insert(self, ele):
        self._elements.append(ele)
        self._bubble_up_recursive(len(self) - 1)
    
    def _bubble_up(self, current_idx):
        current_ele = self._elements[current_idx]
        while current_idx > 0:
            parent_idx = self._parent_index(current_idx)
            parent_ele = self._elements[parent_idx]
            if self._has_higher_priority(current_ele, parent_ele):
                self._swap_list_ele(current_idx, parent_idx)
                current_idx = parent_idx
            else:
                break

    def _bubble_up_recursive(self, current_idx):
        """The same function as abow, while recursively."""
        if current_idx > 0:
            current_ele = self._elements[current_idx]
            parent_idx = self._parent_index(current_idx)
            parent_ele = self._elements[parent_idx]
            if self._has_higher_priority(current_ele, parent_ele):
                self._swap_list_ele(current_idx, parent_idx)
                self._bubble_up_recursive(parent_idx)
    
    def top(self):
        if self.is_empty():
            raise ValueError("Error! Empty Heap")
        if len(self) == 1:
            element = self._elements.pop()
        else:
            element = self._elements[0]
            self._elements[0] = self._elements.pop()
            self._sink_down(0)
        return element

    def _sink_down(self, current_idx):
        need_swap_child_index = self._highest_priority_child_index(current_idx)
        if need_swap_child_index is not None:
            self._swap_list_ele(need_swap_child_index, current_idx)
            self._sink_down(need_swap_child_index)
    
    def _highest_priority_child_index(self, current_idx):
        if self._has_one_child(current_idx):
            left_child_idx = self._left_child_index(current_idx)
            left_child_ele = self._elements[left_child_idx]
            current_ele = self._elements[current_idx]
            if self._has_higher_priority(left_child_ele, current_ele):
                self._swap_list_ele(left_child_idx, current_idx)
                return None
        if self._has_two_child(current_idx):
            current_ele = self._elements[current_idx]
            left_child_idx, right_child_idx = (
                self._left_child_index(current_idx),
                self._right_child_index(current_idx)
            )
            left_child_ele, right_child_ele = (
                self._elements[left_child_idx], 
                self._elements[right_child_idx]
            )
            if (
                self._has_higher_priority(left_child_ele, current_ele) and 
                self._has_higher_priority(left_child_ele, right_child_ele) or
                self._has_equivalent_priority(left_child_ele, right_child_ele) and
                self._has_higher_priority(left_child_ele, current_ele)
            ):
                need_swap_idx = left_child_idx
            elif (
                self._has_higher_priority(right_child_ele, left_child_ele) and
                self._has_higher_priority(right_child_ele, current_ele)
            ):
                need_swap_idx = right_child_idx
            else:
                need_swap_idx = None
            return need_swap_idx

    def _has_lower_priority(self, ele_1, ele_2):
        return self._priority(ele_1) < self._priority(ele_2)
    
    def _has_equivalent_priority(self, ele_1, ele_2):
        return self._priority(ele_1) == self._priority(ele_2)

    def _has_higher_priority(self, ele_1, ele_2):
        return self._priority(ele_1) > self._priority(ele_2)

    def _left_child_index(self, idx):
        return idx * 2 + 1
    
    def _right_child_index(self, idx):
        return idx * 2 + 2
    
    def _parent_index(self, idx):
        return (idx - 1) // 2
    
    def _has_two_child(self, idx):
        return self._right_child_index(idx) < len(self)

    def _has_one_child(self, idx):
        return self._left_child_index(idx) == len(self) - 1
    
    def _heapify(self, elements):
        self._elements = elements[:]
        last_inner_node_index = len(self) // 2 - 1
        for idx in range(last_inner_node_index, -1, -1):
            self._sink_down(idx)

    def _swap_list_ele(self, idx_1, idx_2):
        self._elements[idx_1], self._elements[idx_2] = (
            self._elements[idx_2], 
            self._elements[idx_1]
        )
    
    def is_empty(self):
        return len(self) == 0
    
    def k_largest_elements(self, num):
        return [self.top() for _ in range(num)]



class Item:

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"


PriorityItem = namedtuple("PriorityItem", "priority index item")


class PriorityQueen:

    def __init__(self) -> None:
        self._queue = list()
        self._index = 0

    def push(self, item, priority):
        priority_item = PriorityItem(-priority, self._index, item)
        heapq.heappush(self._queue, priority_item)
        self._index += 1

    def pop(self):
        return getattr(heapq.heappop(self._queue), "item")


def use_priority_queue():
    q = PriorityQueen()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 7)
    q.push(Item("spam"), 5)
    q.push(Item("grokking"), 2)
    q.push(Item("avenge"), 5)
    q.push(Item("reparation"), 7)
    q.push(Item("eloquent"), 12)
    
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


# use_priority_queue()


def test_heap():
    itmes = [
        ("Memory leak", 3), ("Broken login", 8), ("UI break on browser X", 2),
        ("Password Authentication", 10), ("CSS problem", 9),
        ("Optional form field blocked", 7), ("Good gay", 13),
        ("Good Boty", 8), ("Good jsks", 7), ("Good bitcoin", 12),]
    h = Heap(elements=itmes, element_priority=operator.itemgetter(1))
    print(h)
    print(h.k_largest_elements(4))


def n_largest_elements_from_heap(arr, k):
    heap = Heap(arr)
    return [heap.top() for i in range(k)]


def use_heapq_module(arr):
    lst = arr[:]
    heapq.heapify(lst)
    print(lst)
    for _ in range(3):
        print(heapq.heappop(lst))
    print(heapq.nlargest(3, lst))
    print(lst)
    print(heapq.heapreplace(lst, 12))
    print(lst)
    print(heapq.heappushpop(lst, 9))
    print(lst)
    

def heap_merge():
    a = [1, 4, 7, 10, 17]
    b = [2, 5, 6, 13, 19]
    c = sorted([15, 4, 14, 11, 3])
    for item in heapq.merge(a, b, c):
        print(item, end=", ")


# heap_merge()

def read_file(file_path, chunk_size=10):
    import sys
    with open(file=file_path, mode="rt", encoding="utf-8") as fp:
        for chunk in iter(lambda: fp.read(chunk_size), ""):
            sys.stdout.write(chunk)


# read_file("/home/shangguan/Downloads/History.txt")




if __name__ == "__main__":
    ...
    arr = [9, 2, 13, 6, 1, 10, 3, 8, 5, 18, 11, 15, 7]
    # print(n_largest_elements_from_heap(
    #     arr,
    #     5
    # ))
    # use_heapq_module(arr)


