"""
This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""


def next_permutation(num: list) -> list:
    # Note: list will be modified in place
    index = len(num) - 1
    while index > 0:
        if num[index] > num[index - 1]:
            break
        index -= 1
    else:
        num[:] = num[::-1]
        return num
    swap_index = index - 1
    while index < len(num) and num[index] > num[swap_index]:
        index += 1
    num[swap_index], num[index - 1] = num[index - 1], num[swap_index]
    num[swap_index + 1:] = num[-1:swap_index:-1]
    return num


print(next_permutation([1, 2, 3]))  # ANSWER: [1, 3, 2]
print(next_permutation([1, 3, 2]))  # ANSWER: [2, 1, 3]
print(next_permutation([3, 2, 1]))  # ANSWER: [1, 2, 3]
