"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def sorted_square(arr: list) -> list:
    new_arr = []
    i = 0

    # Get the mid index, where negative to positive transition happened
    while arr[i] < 0 and i < len(arr):
        i += 1
    j = i - 1

    if j < 0:
        return list(map(lambda x: x ** 2, arr))
    elif i == len(arr):
        return list(map(lambda x: x ** 2, arr[::-1]))

    # Merge the two lists
    while i < len(arr) and j > -1:
        if arr[i] < abs(arr[j]):
            new_arr.append(arr[i] ** 2)
            i += 1
        else:
            new_arr.append(arr[j] ** 2)
            j -= 1

    new_arr.extend(list(map(lambda x: x ** 2, arr[i:])))
    new_arr.extend(list(map(lambda x: x ** 2, arr[:j + 1][::-1])))

    return new_arr


if __name__ == "__main__":
    print(sorted_square([-9, -2, 0, 2, 3]))  # ANS = [0, 4, 4, 9, 81]
