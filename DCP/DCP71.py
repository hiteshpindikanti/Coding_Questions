"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
from random import choice


def rand7() -> int:
    return choice(range(1, 8))


def rand5() -> int:
    ans = rand7()
    while ans > 5:
        ans = rand7()
    return ans
