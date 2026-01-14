

class QueueUnderFlow(IndexError):
    pass


class MinHeap:

    def __init__(self) -> None:
        self.heap: list = [0]
        self.size = 0

    def heapify(self, k):
        """ After modifying the heap tree, rearrange the node to adhere to the heap property,
            from the bottom to the top.
        """
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            else:
                break
            k //= 2

    def heapify_recursive(self, k):
        if k != 1:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
                self.heapify_recursive(k // 2)
    
    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify(self.size)
    
    def get_min_child(self, k):
        if k * 2 + 1 > self.size:
        # check if wo get beyond the end of the list
            return k * 2
        else:
            if self.heap[k * 2] < self.heap[k * 2 + 1]:
                return k * 2
            else:
                return k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.get_min_child(k=k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def sink_recursive(self, k):
        if k * 2 <= self.size:
            min_child_k = self.get_min_child(k=k)
            if self.heap[k] > self.heap[min_child_k]:
                self.heap[k], self.heap[min_child_k] = self.heap[min_child_k], self.heap[k]
                self.sink_recursive(min_child_k)
            else:
                return

    def delete_root(self):
        root_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()   # delete the last item 
        self.sink(1)
        return root_value

    def delete_at_index(self, index):
        item = self.heap[index]
        self.heap[index] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink_recursive(index)
        return item

    def heap_sort(self):
        sorted_list = []
        for _ in range(self.size):
            sorted_list.append(self.delete_root())
        return sorted_list


def min_heap():
    mh = MinHeap()
    dataset = (4, 8, 7, 2, 9, 10, 5, 1, 3, 6)
    for i in dataset:
        mh.insert(i)
    print(mh.heap)
    print(mh.delete_root())
    print(mh.heap)
    print(mh.heap_sort())


class MaxHeap:

    def __init__(self) -> None:
        self._elements = list()
        self._count = 0
    
    def __len__(self):
        return self._count
    
    def __str__(self) -> str:
        return ", ".join(str(ele) for ele in self._elements)
    
    def __contains__(self, value):
        return value in self._elements

    def __eq__(self, other):
        pass

    def __iter__(self):
        pass

    def __add__(self, other):
        pass

    def capacity(self):
        return len(self._elements)
    
    def peek(self):
        return self._elements[0]

    def insert(self, value):
        self._elements.append(value)
        self._count += 1
        self._sift_up(self._count - 1)

    def extract(self):
        assert self._count > 0
        root_value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._sift_down(0)
        return root_value
    
    def is_empty(self):
        return self._count == 0
    
    def _swap(self, idx_1, idx_2):
        self._elements[idx_1], self._elements[idx_2] = (
            self._elements[idx_2],
            self._elements[idx_1]
        )

    def _sift_up(self, idx):
        if idx > 0:
            parent = (idx - 1) // 2
            if self._elements[idx] > self._elements[parent]:
                self._swap(idx, parent)
                self._sift_up(parent)

    def _sift_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if (
            left < self._count and
            self._elements[left] >= self._elements[largest]
        ):
            largest = left
        if (
            right < self._count and 
            self._elements[right] >= self._elements[largest]
        ):
            largest = right
        if largest != idx:
            self._swap(idx, largest)
            self._sift_down(largest)


def test_heap_max():
    dataset = [5, 7, 4, 1, 9, 3, 6, 11, 2, 8]
    max_heap = MaxHeap()
    for value in dataset:
        max_heap.insert(value)
    print(max_heap)
    print(max_heap.extract())
    print(max_heap.extract())
    print(max_heap.extract())
    print(max_heap)


# test_heap_max()


def heap_sort(seq):
    """heap sort a sequence in place"""
    length = len(seq)

    def swap(idx_1, idx_2):
        seq[idx_1], seq[idx_2] = seq[idx_2], seq[idx_1]

    def sift_up(idx):
        if idx > 0:
            parent = (idx - 1) // 2
            if seq[idx] > seq[parent]:
                swap(idx, parent)
                sift_up(parent)

    def sift_down(upper_index, idx):
        largest = idx
        left = 2 * largest + 1
        right = 2 * largest + 2
        if left <= upper_index:
            if right <= upper_index:
                if seq[largest] <= max(seq[left], seq[right]):
                    if seq[left] < seq[right]:
                        largest = right
                    else:
                        largest = left
            else:
                if seq[left] >= seq[largest]:
                    largest = left
        if idx != largest:
            swap(idx, largest)
            sift_down(upper_index, largest)
    
    for i in range(length):
        sift_up(i)
    
    for j in range(length - 1, 0, -1):
        swap(0, j)
        sift_down(j - 1, 0)
    

# li = [23, 10, 51, 13, 2, 18, 13, 4, 31, 13, 5, 23, 64, 23, 29]
# heap_sort(li)
# print(li)


class PriorityQueueNode:

    def __init__(self, info, priority) -> None:
        self.info = info
        self.priority = priority
    
    def __str__(self) -> str:
        return f"[priority {self.priority}] - ({self.info})"
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other) -> bool:
        return self.priority == other.priority


class PriorityQueue:

    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for x in range(0, len(self.queue)):
                if node.priority >= self.queue[x].priority:
                    if x == (len(self.queue) - 1):
                        self.queue.insert(x + 1, node)
                else:
                    self.queue.insert(x, node)
                    return
    
    def dequeue(self):
        node = self.queue.pop(0)
        print(f"Dequeue node {node.info!r} with the [priority - {node.priority}]")
        return node

    def show_queue(self):
        for node in self.queue:
            print(node)


def priority_queue():
    dataset = [
        ("Cat", 11),
        ("Bat", 9),
        ("Dog", 13),
        ("Rat", 4),
        ("Lion", 12),
        ("Ant", 7),
        ("Mouse", 10),
    ]
    p = PriorityQueue()
    for item in dataset:
        p.enqueue(PriorityQueueNode(*item))
    p.show_queue()
    p.dequeue()
    p.dequeue()


class PriorityQueueHeap:

    def __init__(self) -> None:
        self.heap = [(-1,None)]
        self.size = 0
    
    def heapify(self, k):
        if k != 1:
            if self.heap[k][0] < self.heap[k // 2][0]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
                self.heapify(k // 2)
            else:
                return
    
    def enqueue(self, priority, item):
        self.heap.append((priority, item))
        self.size += 1
        self.heapify(self.size)


    def get_min_child(self, k):
        if k * 2 + 1 > self.size:
        # check if wo get beyond the end of the list
            return k * 2
        else:
            if self.heap[k * 2][0] < self.heap[k * 2 + 1][0]:
                return k * 2
            else:
                return k * 2 + 1

    def sink(self, k):
        if k * 2 <= self.size:
            min_child_k = self.get_min_child(k=k)
            if self.heap[k][0] > self.heap[min_child_k][0]:
                self.heap[k], self.heap[min_child_k] = self.heap[min_child_k], self.heap[k]
                self.sink(min_child_k)
            else:
                return
    
    def dequeue(self):
        if self.size == 0:
            raise QueueUnderFlow("dequeue failed, empty queue")
        else:
            node = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.heap.pop()
            self.sink(1)
            return node
    
    def show(self):
        for _ in range(self.size):
            print(self.dequeue())


def priority_heap():
    dataset = [
        ("Cat", 11),
        ("Bat", 9),
        ("Dog", 13),
        ("Rat", 4),
        ("Lion", 12),
        ("Ant", 7),
        ("Mouse", 10),
    ]
    p = PriorityQueueHeap()
    for i in dataset:
        p.enqueue(i[1], i[0])
    print(p.heap)
    for _ in range(3):
        print(p.dequeue())


class PriorityQueueMinHeap:

    def __init__(self) -> None:
        self._heap = MinHeap()

    def enqueue(self, data, priority):
        node = PriorityQueueNode(data, priority)
        self._heap.insert(node)

    def dequeue(self):
        if not self.is_empty():
            node = self._heap.delete_root()
            return node
        else:
            raise QueueUnderFlow("empty queue")

    def is_empty(self):
        return self._heap.size == 0



def test_priority_queue_min_heap():
    priority_queue_min_heap = PriorityQueueMinHeap()
    priority_queue_min_heap.enqueue("Black", 2)
    priority_queue_min_heap.enqueue("white", 1)
    priority_queue_min_heap.enqueue("green", 5)
    priority_queue_min_heap.enqueue("red", 4)
    priority_queue_min_heap.enqueue("yellow", 7)
    priority_queue_min_heap.enqueue("pink", 1)
    priority_queue_min_heap.enqueue("violet", 0)
    priority_queue_min_heap.enqueue("orange", 5)

    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())
    print(priority_queue_min_heap.dequeue())


# test_priority_queue_min_heap()


if __name__ == "__main__":
    # priority_queue()
    # priority_heap()
    pass