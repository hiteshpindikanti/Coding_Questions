"""
This problem was asked by Facebook.

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.
"""
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def f():
    print("Hello World")


class Debounced:
    lock = False
    n = 500
    f = None

    def __init__(self, f, N):
        Debounced.n = N
        Debounced.f = f
        pass

    @staticmethod
    def fun():
        if not Debounced.lock:
            Debounced.lock = True
            sleep(Debounced.n)
            Debounced.f()
            Debounced.lock = False


# Approach 2
def debounced(time):
    lock = False

    def inner(func):
        def wrapper():
            nonlocal lock
            if not lock:
                lock = True
                sleep(time / 1000)
                func()
                lock = False

        return wrapper

    return inner


@debounced(500)
def f():
    print('hello world')


if __name__ == "__main__":
    ThreadPoolExecutor().submit(f)
    ThreadPoolExecutor().submit(f)
    sleep(1)
    ThreadPoolExecutor().submit(f)
    ThreadPoolExecutor().submit(f)

    # obj = Debounced(lambda: print("Hello World"), 500 / 1000)
    # ThreadPoolExecutor().submit(obj.fun)
    # sleep(1)
    # ThreadPoolExecutor().submit(obj.fun)
    # sleep(1)
    # ThreadPoolExecutor().submit(obj.fun)
