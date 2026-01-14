
from doubly_list import DoublyLinkedListNode


class CircularLinkedListNode(DoublyLinkedListNode):
    pass


class CircularLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = CircularLinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            pass


