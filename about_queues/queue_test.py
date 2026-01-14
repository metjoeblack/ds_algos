
from queue_stacks.many_queues import Queue, Stack, PriorityQueue


def use_queue_stack():
    fifo = Queue("1st", "2nd", "3rd", "4th")
    print(len(fifo))

    for element in fifo:
        print(element)
    print(len(fifo))
    print(fifo.is_empty())

    lifo = Stack("1st", "2nd", "3rd", "4th")
    for ele in lifo:
        print(ele)


def use_priority_queue():
    pq = PriorityQueue()
    pq.enqueue("a", 1)
    pq.enqueue("c", 2)
    pq.enqueue(3.14, 5)
    pq.enqueue('d', 2)
    pq.enqueue(100, 4)
    pq.enqueue('f', 4)
    pq.enqueue(b'Python', 1)

    for val in pq:
        print(val)



if __name__ == '__main__':
    use_queue_stack()
    use_priority_queue()
    pass