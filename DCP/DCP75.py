"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""


def longest_subsequence_length(arr: list) -> int:
    memory = []
    for val in arr:
        for i in range(len(memory)):
            if memory[i][1] < val:
                memory.append((memory[i][0] + 1, val))
        memory.append((1, val))
    return max(memory)[0]


def longest_subsequence_length_rec(arr):
    if len(arr) == 1:
        return 1, arr[-1]
    table = [(1, arr[0])]
    for j in range(1, len(arr)):
        answer = (0, 0)
        for i in range(j):
            length_i, last_element_i = table[i]
            if arr[j] > last_element_i and answer[0] < length_i + 1:
                answer = (length_i + 1, arr[j])
        table.append(answer)
    return table[-1][0]


print(longest_subsequence_length_rec([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
