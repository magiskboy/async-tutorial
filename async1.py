import threading
import time


def countdown(n):
    while n > 0:
        print("Down", n)
        time.sleep(1)
        n -= 1


def countup(stop):
    n = 0
    while n < stop:
        print("Up", n)
        time.sleep(1)
        n += 1


# Sequence
# countup(5)
# countdown(5)

# Concurrency within threads
# threading.Thread(target=countup, args=(5,)).start()
# threading.Thread(target=countdown, args=(5,)).start()
