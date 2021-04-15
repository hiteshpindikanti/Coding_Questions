"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import concurrent.futures
from time import sleep
import functools


def f():
    print("function f is called")


def scheduler(func, n):
    print("start n={}".format(n))
    sleep(n)
    func()
    print("end n={}".format(n))


arr = list(map(lambda x: x/100, [1, 5, 10, 100, 350]))
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(functools.partial(scheduler, f), arr)
