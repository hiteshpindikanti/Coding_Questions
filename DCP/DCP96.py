"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def get_permutations(num: list) -> list:
    if not num:
        return [[]]

    permutations = []
    for index, digit in enumerate(num):
        permutations.extend(list(map(lambda x: [digit] + x, get_permutations(num[:index]+num[index+1:]))))
    return permutations


print(get_permutations([1]))
print(get_permutations([1, 2, 3]))
