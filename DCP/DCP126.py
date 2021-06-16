"""
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?
"""


def rotate(array: list, k: int) -> None:
    array_length = len(array)
    k = k % array_length
    reverse(array, 0, k - 1)
    reverse(array, k, array_length - 1)
    reverse(array, 0, array_length - 1)


def reverse(array: list, start_index: int, end_index: int) -> None:
    while start_index < end_index:
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7]
    print(f'Before: {l}')
    rotate(l, 2)
    print(f'After: {l}')
