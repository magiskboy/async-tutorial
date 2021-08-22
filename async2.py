import time
from collections import deque
import heapq


class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self.sequence = 0

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, later, func):
        self.sequence += 1
        deadline = later + time.time()
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline, _, func = self.sleeping.pop(0)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)

            if self.ready:
                func = self.ready.popleft()
                func()


sched = Scheduler()


def countdown(n):
    if n > 0:
        print("Down", n)
        sched.call_later(2, lambda: countdown(n - 1))


def countup(stop, n=0):
    if n < stop:
        print("Up", n)
        sched.call_later(1, lambda: countup(stop, n + 1))


sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()
