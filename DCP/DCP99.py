"""
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def get_longest_consecutive_sequence_length(arr: list):
    arr_set = set(arr)
    visited = set()
    max_count = 0
    for index in range(len(arr)):
        if arr[index] not in visited:
            count = 1

            # Back search
            num = arr[index] - 1
            while num in arr_set:
                visited.add(num)
                num -= 1
                count += 1

            # Forward Search
            num = arr[index] + 1
            while num in arr_set:
                visited.add(num)
                num += 1
                count += 1

            max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    lst = [100, 4, 200, 1, 3, 2]
    print(get_longest_consecutive_sequence_length(lst))  # answer=4
