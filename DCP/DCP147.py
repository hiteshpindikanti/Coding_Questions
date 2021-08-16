"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""
from random import randint


def reverse(lst, i, j):
    for start_index in range(i, j // 2 + 1):
        end_index = j - (start_index - i)
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index]


def reverse_sort(lst):

    pass


if __name__ == "__main__":
    l = [randint(1, 100) for _ in range(10)]
    print(f"BEFORE: {l}")
    reverse_sort(l)
    print(f"AFTER: {l}")
