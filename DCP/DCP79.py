"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""


def can_be_modified(array: list) -> bool:
    is_under_limit = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            if is_under_limit:
                is_under_limit = False
            else:
                return False
    return True


print(can_be_modified([10, 5, 7]))
print(can_be_modified([10, 5, 1]))
