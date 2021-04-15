"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def find(arr: list, n: int) -> int:
    # Find the middle element with binary search
    start = 0
    end = len(arr) - 1
    while end - start > 1:
        mid = (start + end) // 2
        if arr[mid] > arr[end]:
            start = mid
        elif arr[mid] < arr[end]:
            end = mid

    shift = end
    start = (0 + shift) % len(arr)
    end = (len(arr) - 1 + shift) % len(arr)

    while start != end:
        mid = end - start if end > start else (start + (len(arr) - start + end + 1) // 2) % len(arr)
        if n == arr[mid]:
            return mid
        elif n == arr[start]:
            return start
        elif n == arr[end]:
            return arr[end]
        elif mid == start:
            return -1
        elif n > arr[mid]:
            start = (mid + 1) % len(arr)
            end = (end + len(arr) - 1) % len(arr)
        elif n < arr[mid]:
            start = (start + 1) % len(arr)
            end = (mid + len(arr) - 1) % len(arr)


print(find([13, 18, 25, 2, 8, 10], 8))
