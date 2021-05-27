"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""
from queue import Queue


def get_sublist(l: list, k: int) -> list:
    result_list = Queue()
    current_sum = 0
    for element in l:
        if current_sum < k:
            result_list.put(element)
            current_sum += element
        if current_sum > k:
            current_sum -= result_list.get()
        if current_sum == k:
            return list(result_list.queue)
    return []


print(get_sublist([1, 2, 3, 4, 5], 9))
