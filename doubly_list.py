
from typing import Generator
import heapq


class EmptyLinkedListError(ValueError):
    pass


class DoublyLinkedListNode:

    def __init__(self, data=None) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
    def __lt__(self, other):
        return self.data < other.data
    
    def __eq__(self, other) -> bool:
        return self.data == other.data

    def __repr__(self) -> str:
        return f"{type(self).__name__}(data={self.data!r})"
    
    def __str__(self) -> str:
        return f"{self.data!r}"


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __contains__(self, value):
        for node in self:
            if node.has_value(value=value):
                return True
        return False

    def __len__(self):
        return self.count
    
    def counts(self, value):
        counter = 0
        for node in self:
            if node.has_value(value):
                counter += 1
        return counter

    def traverse(self) -> Generator:
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def reverse_traverse(self) -> Generator:
        current = self.tail
        while current:
            yield current.data
            current = current.prev
    
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
    
    def append(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def appendleft(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def insert(self, index, value):
        if index > self.count or index < 0:
            raise IndexError(f"index {index} out of range")
        if index == 0:
            self.appendleft(value=value)
        elif index == self.count:
            self.append(value=value)
        else:
            new_node = DoublyLinkedListNode(value)
            current_node = prev_node = self.head
            temp_counter = 0
            while current_node:
                if index == temp_counter:
                    prev_node.next = new_node
                    new_node.prev = prev_node
                    new_node.next = current_node
                    current_node.prev = new_node
                temp_counter += 1
                prev_node = current_node
                current_node = current_node.next
            self.count += 1

    def pop(self):
        if not self.is_empty():
            current = self.tail
            temp = current.data
            self.tail = current.prev
            self.tail.next = None
            del current
            self.count -= 1
            return temp

    def popleft(self):
        if not self.is_empty():
            current = self.head
            temp = current.data
            self.head = current.next
            self.head.prev = None
            del current
            self.count -= 1
            return temp
    
    def delete(self, value):
        if not self.is_empty():
            if self.head.has_value(value):
                self.popleft()
            elif self.tail.has_value(value):
                self.pop()
            else:
                current = self.head
                while current:
                    if current.has_value(value):
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        self.count -= 1
                        break
                    current = current.next
                else:
                    raise ValueError(f"Value {value!r} not found in the list")

    def delete_all(self, value):
        pass

    def reverse(self):
        if self.count > 1:
            temp_tail = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            current = self.head
            current.prev = temp_tail
            temp_tail.next = current
            temp_tail.prev = None
            self.head = temp_tail
            while current is not self.tail:
                leftmost_of_current = current.prev
                temp_tail = self.tail
                self.tail.prev.next = None
                self.tail = self.tail.prev
                current.prev = temp_tail
                temp_tail.next = current
                leftmost_of_current.next = temp_tail
                temp_tail.prev = leftmost_of_current

    def is_empty(self):
        if self.count == 0:
            raise EmptyLinkedListError("Empty doubly linked list")
        else:
            return False


def test(dataset):
    dou = DoublyLinkedList()
    dou.extend(dataset)
    print(list(dou.traverse()))
    print(list(dou.reverse_traverse()))
    print(sorted(dou))
    # dou.append("one")
    # dou.traverse()
    # dou.appendleft("zero")
    # dou.traverse()
    # dou.insert(0, "begin")
    # dou.traverse()
    # dou.insert(2, "two")
    # dou.traverse()
    # dou.insert(4, "four")
    # dou.traverse()
    # print(dou.count)
    # dou.insert(8, "ab")
    # dou.traverse()
    # print(dou.pop())
    # dou.traverse()
    # print(dou.count)
    # print(dou.popleft())
    # dou.traverse()
    # print(dou.count)
    # dou.delete("two")
    # dou.traverse()
    # print(dou.count)
    # dou.delete("zero")
    # dou.traverse()
    # print(dou.count)
    # dou.traverse()
    # print(dou.count)
    # print(dou.head.data)
    # print(dou.tail.data)
    # dou.traverse()
    # print(dou.count)
    # print(dou.counts("ab"))


if __name__ == "__main__":
    dataset = ["ab", "cd", "ef", "gh", "ij", "kl"]
    dataset = [4, 7, 1, 3, 2, 5, 9, 6, 8]
    test(dataset)




