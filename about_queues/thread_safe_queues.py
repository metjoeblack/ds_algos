
import argparse
import time
import threading

from queue import LifoQueue, PriorityQueue, Queue
from contextlib import suppress
from random import randint, choice
from itertools import zip_longest

from rich.align import Align
from rich.console import Group
from rich.columns import Columns
from rich.live import Live
from rich.panel import Panel


QUEUE_TYPES = {"fifo": Queue, "lifo": LifoQueue, "pq": PriorityQueue}

PRODUCTS = (
    ":balloon:", ":cookie:", ":crystal_ball:", ":diving_mask:",
    ":flashlight:", ":gem:", ":gift:", ":kite:", ":party_popper:",
    ":postal_horn:", ":ribbon:", ":rocket:", ":teddy_bear:", ":thread:",
    ":yo-yo:", ":zap:", ":zebra:", ":zombie:"
)

def parse_cmd_args():
    parser = argparse.ArgumentParser(
        prog="Thread-Safe-Queues",
        description="A simple queue using a producer-consumer model",
    )
    parser.add_argument("-q", '--queue', choices=QUEUE_TYPES, default='fifo')
    parser.add_argument("-p", '--producers', type=int, default=3)
    parser.add_argument("-c", '--consumers', type=int, default=2)
    parser.add_argument("-ps", '--producer-speed', type=int, default=1)
    parser.add_argument("-cs", '--consumer-speed', type=int, default=1)
    return parser.parse_args()


class View:
    def __init__(self, buffer, producers, consumers):
        self.buffer = buffer
        self.producers = producers
        self.consumers = consumers

    def animate(self):
        with Live(self.render(), screen=True, refresh_per_second=10) as live:
            while True:
                live.update(self.render())
                time.sleep(0.1)     # Prevent CPU overuse.

    def render(self):
        match self.buffer:
            case PriorityQueue():
                title = "Priority Queue"
                products = list(map(str, reversed(list(self.buffer.queue))))
            case LifoQueue():
                title = "Stack"
                products = list(self.buffer.queue)
            case Queue():
                title = "Queue"
                products = [str(p) for p in reversed(list(self.buffer.queue))]
            case _:
                title, products = "", []

        rows = [
            Panel(f"[bold]{title}:[/] {', '.join(products)}", width=82)
        ]
        pairs = zip_longest(self.producers, self.consumers)
        for idx, (producer, consumer) in enumerate(pairs, start=1):
            left_panel = self.panel(producer, f"Producer {idx}")
            right_panel = self.panel(consumer, f"Consumer {idx}")
            rows.append(Columns([left_panel, right_panel], width=40))
        return Group(*rows)

    @staticmethod
    def panel(worker, title):
        if worker is None:
            return Panel("", height=5, title=title)
        padding = " " * int(29 / 100 * worker.progress)
        align = Align(
            padding + worker.state, align="left", vertical="middle"
        )
        return Panel(align, height=5, title=title)


class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.is_working = False
        self.progress = 0

    @property
    def state(self):
        if self.is_working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: Idle"

    def simulate_idle(self):
        self.product = None
        self.is_working = False
        self.progress = 0
        time.sleep(randint(1, 3))

    def simulate_work(self):
        self.is_working = True
        self.progress = 0
        delay = randint(1, 1 + 15 // self.speed)
        for _ in range(100):
            time.sleep(delay / 100)
            self.product += 1


class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products
    def run(self):
        while True:
            self.product += choice(self.products)
            self.simulate_work()
            self.buffer.put(self.product)
            self.simulate_idle()


class Consumer(Worker):
    def run(self):
        while True:
            self.product = self.buffer.get(timeout=3)
            self.simulate_work()
            self.buffer.task_done()
            self.simulate_idle()


def main(args):
    # args = parse_cmd_args()
    # print(args)
    # with suppress(KeyboardInterrupt):
    #     buffer = QUEUE_TYPES.get(args.queue)()
    # print(buffer)
    buffer = QUEUE_TYPES.get(args.queue)()
    producers = [
        Producer(args.producer_speed, buffer, PRODUCTS)
        for _ in range(args.producers)
    ]
    consumers = [
        Consumer(args.consumer_speed, buffer)
        for _ in range(args.consumers)
    ]
    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()


if __name__ == '__main__':
    # --producers 3 --consumers 2 --producer-speed 1 --consumer-speed 1 --queue fifo
    with suppress(KeyboardInterrupt):
        main(parse_cmd_args())
