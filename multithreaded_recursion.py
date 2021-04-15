import concurrent.futures
import time
from random import randint
import sys


def find_min(l: list) -> int:
    if len(l) == 2:
        return min(*l)
    else:
        return min(l[0], find_min(l[1:]))

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    list_size = 10 ** 4
    lst = [randint(1, 1000) for _ in range(list_size)]

    # Normal Iterative Approach
    start_time = time.time()
    min_element = min(lst)
    end_time = time.time()
    print("list_size = {}, smallest_element = {}, time_taken = {} secs"
          .format(list_size, min_element, end_time - start_time))

    # Recursive Approach
    start_time = time.time()
    min_element = find_min(lst)
    end_time = time.time()
    print("list_size = {}, smallest_element = {}, time_taken = {} secs"
          .format(list_size, min_element, end_time - start_time))



