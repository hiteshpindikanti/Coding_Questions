"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def get_nearest_larger_number(array: list, index: int) -> int:
    right = float('inf')
    left = float('-inf')
    for i in range(index+1, len(array)):
        if array[i] > array[index]:
            right = i
            break

    for i in range(index-1, -1, -1):
        if array[i] > array[index]:
            left = i
            break

    if right-index < index-left:
        return right if right != float('-inf') else None
    else:
        return left if left != float('inf') else None

def get_nearest_larger_number_preprocess(array: list, index: int) -> int:
    # preprocess
    enumerate(array)
if __name__ == "__main__":
    assert get_nearest_larger_number([4, 1, 3, 5, 6], 0) == 3

