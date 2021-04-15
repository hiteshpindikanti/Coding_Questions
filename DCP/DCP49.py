"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""


def max_sum_subarray(arr: list) -> int:
    for i in range(1, len(arr)):
        arr[i] = max(arr[i - 1] + arr[i], arr[i])
    return max(max(arr),0)


print(max_sum_subarray([34, -50, 42, 14, -5, 86]))
print(max_sum_subarray([-5, -1, -8, -9]))
