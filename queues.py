import ctypes

class Array1D:

    def __init__(self, size) -> None:
        assert size > 0
        self._size = size

        # Create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear(None)
    
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self)
        return self._elements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self)
        self._elements[index] = value
    
    def clear(self, value=None):
        """Clears the array by setting each element to the given value."""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return self._ArrayIterator(self._elements)

    class _ArrayIterator:
        
        def __init__(self, the_array) -> None:
            self._array_ref = the_array
            self._current_index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._current_index < len(self._array_ref):
                entry = self._array_ref[self._current_index]
                self._current_index += 1
                return entry
            else:
                raise StopIteration


class QueueOverFlow(IndexError):
    pass


class QueueUnderFlow(IndexError):
    pass


class ListBasedQueue:

    def __init__(self, size=4) -> None:
        self.items = []
        self.front = self.rear = 0   # index record
        self.size = size             # the fixed length
    
    def __str__(self) -> str:
        return " ".join(str(i) for i in self.items)

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        if self.rear == self.size:
            raise QueueOverFlow(f"queue's length is {self.size}, full now")
        else:
            self.items.append(value)
            self.rear += 1

    def dequeue(self):
        if self.rear == self.front:
            raise QueueUnderFlow("can't dequeue, queue is empty now")
        else:
            self.rear -= 1
            return self.items.pop(self.front)
    
    def is_full(self):
        return len(self) == self.size
    
    def is_empty(self):
        return len(self) == 0
    


def test_1():
    lbq = ListBasedQueue(size=5)
    print(lbq.is_empty())
    lbq.enqueue(10)
    lbq.enqueue(20)
    lbq.enqueue(30)
    lbq.enqueue(40)
    lbq.enqueue(50)
    print(lbq.is_full())
    print(lbq)
    print(lbq.dequeue())
    print(lbq.dequeue())
    print(lbq.dequeue())
    print(lbq.dequeue())
    print(lbq)



class LinkedListBasedQueue:

    class QueueNode(object):

        def __init__(self, data=None) -> None:
            self.data = data
            self.next = self.prev = None

    def __init__(self) -> None:
        self.front = self.rear = None
        self.size = 0
    
    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next
    
    def __str__(self) -> str:
        return " ".join(str(node.data) for node in self)

    def enqueue(self, value):
        new_node = self.QueueNode(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderFlow("can't dequeue, queue is empty now")
        else:
            current = self.front
            self.front = current.next
            current.next.prev = None
            self.size -= 1
            return current.data
    
    def is_empty(self):
        return self.size == 0


def test_2():
    linked_que = LinkedListBasedQueue()
    linked_que.enqueue("one")
    linked_que.enqueue("two")
    linked_que.enqueue("three")
    print(linked_que)
    linked_que.enqueue("four")
    linked_que.enqueue("five")
    print(linked_que)
    print(linked_que.dequeue())
    print(linked_que)
    print(linked_que.dequeue())
    print(linked_que)
    print(linked_que.size)


class CicularQueue:

    def __init__(self, max_size) -> None:
        self._count = 0
        self._front = 0
        self._back = max_size - 1
        self._qArray = Array1D(max_size)
    
    def is_empty(self):
        return self._count == 0
    
    def is_full(self):
        return self._count == len(self._qArray)
    
    def __len__(self):
        return self._count
    
    def enqueue(self, item):
        assert not self.is_full()
        max_size = len(self._qArray)
        self._back = (self._back + 1) % max_size
        self._qArray[self._back] = item
        self._count += 1
    
    def dequeue(self):
        assert not self.is_empty()
        item = self._qArray[self._front]
        max_size = len(self._qArray)
        self._front = (self._front + 1) % max_size
        self._count -= 1
        return item



class BasedListPriorityQueue:

    class _PriorityQueueEntry:

        def __init__(self, item, priority) -> None:
            self.item = item
            self.priority = priority
        
        def __str__(self) -> str:
            return f"([{self.priority}] - {self.item!r})"

    def __init__(self) -> None:
        self._queue_lst = list()
    
    def __str__(self) -> str:
        return ", ".join(str(entry) for entry in self._queue_lst)

    def __len__(self):
        return len(self._queue_lst)
    
    def enqueue(self, data, priority):
        entry = self._PriorityQueueEntry(data, priority)
        if self.is_empty():
            self._queue_lst.append(entry)
        for index, item in enumerate(self._queue_lst, start=0):
            if priority < item.priority:
                self._queue_lst.insert(index, entry)
                break
        else:
            self._queue_lst.append(entry)

    def dequeue(self):
        if not self.is_empty():
            return self._queue_lst.pop(0).item
        else:
            raise QueueUnderFlow("can't dequeue, queue is empty now")
    
    def is_empty(self):
        return len(self) == 0


def test_based_list_pqueue():
    p_queue = BasedListPriorityQueue()
    p_queue.enqueue("orang", 3)
    p_queue.enqueue("black", 1)
    p_queue.enqueue("purple", 5)
    p_queue.enqueue("white", 0)
    p_queue.enqueue("yellow", 5)
    p_queue.enqueue("green", 6)
    p_queue.enqueue("red", 0)
    p_queue.enqueue("pink", 1)
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)


class BasedLinkedListPriorityQueue:

    class _QueueNode:

        def __init__(self, data, priority) -> None:
            self.data = data
            self.priority = priority
            self.next = None

        def __str__(self) -> str:
            return f"([{self.priority}] - {self.data})"

    def __init__(self) -> None:
        self._size = 0
        self.front = self.rear = None

    def is_empty(self):
        return self._size == 0
    
    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next
    
    def __str__(self) -> str:
        return ", ".join(str(node) for node in self)

    def __len__(self):
        return self._size

    def enqueue(self, item, priority):
        new_node = self._QueueNode(item, priority)
        if self.rear is None:
            self.front = self.rear = new_node
        elif self.rear is self.front:
            if priority < self.front.priority:
                self.front = new_node
                new_node.next = self.rear
            else:
                self.front.next = new_node
                self.rear = new_node
        else:
            if priority < self.front.priority:
                new_node.next = self.front
                self.front = new_node
            current = prev = self.front
            while current.next:
                prev = current
                current = current.next
                if priority < current.priority:
                    prev.next = new_node
                    new_node.next = current
                    break
            else:
                self.rear.next = new_node
                self.rear = new_node
        self._size += 1

    def dequeue(self):
        if not self.is_empty():
            current = self.front
            self.front = current.next
            temp = current.data
            del current
            self._size -= 1
            return temp
        else:
            raise QueueUnderFlow("can't dequeue, queue is empty now")


def test_linked_list_queue():
    p_queue = BasedLinkedListPriorityQueue()
    p_queue.enqueue("orang", 3)
    p_queue.enqueue("black", 1)
    p_queue.enqueue("purple", 5)
    p_queue.enqueue("white", 0)
    p_queue.enqueue("yellow", 5)
    p_queue.enqueue("green", 6)
    p_queue.enqueue("red", 0)
    p_queue.enqueue("pink", 1)
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue)



class BoundedPriorityQueue:

    def __init__(self, num_levels) -> None:
        self._queue_size = 0
        self._queue_priority_levels = Array1D(num_levels)
        for i in range(num_levels):
            self._queue_priority_levels[i] = LinkedListBasedQueue()
    
    def __len__(self):
        return self._queue_size
    
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, data, priority):
        if 0 <= priority < len(self._queue_priority_levels):
            self._queue_priority_levels[priority].enqueue(data)
            self._queue_size += 1
        else:
            raise ValueError(f"priority {priority} out of range")

    def dequeue(self):
        assert not self.is_empty()
        i = 0
        p = len(self._queue_priority_levels)
        while i < p and not self._queue_priority_levels[i].is_empty():
            i += 1
        self._queue_size -= 1
        return self._queue_priority_levels[i].dequeue()



class StudentMultiListNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next_by_id = None
        self.next_by_name = None


if __name__ == "__main__":
    # test_1()
    # test_2()
    # test_based_list_pqueue()
    # test_linked_list_queue()
    pass


