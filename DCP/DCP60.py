"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""
from copy import deepcopy


def is_partitionable(s: list, a: int = 0, b: int = 0) -> bool:
    if s:
        s_copy = deepcopy(s)
        e = s_copy.pop()
        return is_partitionable(s_copy, a + e, b) or is_partitionable(s_copy, a, b + e)
    elif a == b:
        return True
    else:
        return False


print(is_partitionable([1, 2, 3]))
print(is_partitionable([15, 5, 20, 10, 35, 15, 10]))
print(is_partitionable([15, 5, 20, 10, 35]))
