"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""
from math import factorial


def num_ways(n: int, m: int) -> int:
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


print(num_ways(2, 2))
print(num_ways(5, 5))
