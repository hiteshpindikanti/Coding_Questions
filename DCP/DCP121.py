"""
This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""
import numpy as np


def can_be_palindrome(string: str, i: int, j: int, k: int) -> bool:
    if i >= j:
        return True
    elif string[i] == string[j]:
        return can_be_palindrome(string, i + 1, j - 1, k)
    elif k > 0:
        return can_be_palindrome(string, i + 1, j, k - 1) or can_be_palindrome(string, i, j - 1, k - 1)
    else:
        return False


# def can_be_palindrome_iterative(string: str, max_deletions: int) -> bool:
#     stack = [(0, len(string) - 1, max_deletions)]
#
#     # table[i][j][k]; k = {0: if k=0, 1: if k>0}
#     table = np.array([None] * 2 * len(string) * len(string)).reshape((len(string), len(string), 2))
#
#     while stack:
#         i, j, k = stack.pop()
#
#         if i >= j:
#             table[i][j] = [True, True]
#         elif string[i] == string[j]:
#             if table[i + 1][j - 1][1 if k > 0 else 0] is not None:
#                 table[i][j][1 if k > 0 else 0] = table[i + 1][j - 1][1 if k > 0 else 0]
#             else:
#                 stack.append((i, j, k))
#                 stack.append((i + 1, j - 1, k))
#         elif k > 0:
#             if table[i + 1][j][1 if k - 1 > 0 else 0] is not None:
#                 if table[i + 1][j][1 if k - 1 > 0 else 0]:
#                     table[i][j][1 if k > 0 else 0] = True
#                 else:
#                     if table[i][j - 1][1 if k - 1 > 0 else 0] is not None:
#                         if table[i][j - 1][1 if k - 1 > 0 else 0]:
#                             table[i][j][1 if k > 0 else 0] = True
#                         else:
#                             table[i][j][1 if k > 0 else 0] = False
#                     else:
#                         stack.append((i, j, k))
#                         stack.append((i, j - 1, k - 1))
#             else:
#                 stack.append((i, j, k))
#                 stack.append((i + 1, j, k - 1))
#     return any(table[0][len(string) - 1])
#

def can_be_palindrome_iterative2(string: str, max_deletions: int) -> bool:
    stack = [(0, len(string) - 1, max_deletions)]

    # table[i][j][k]; k = {0: if k=0, 1: if k>0}
    table = np.array([None] * 2 * len(string) * len(string)).reshape((len(string), len(string), 2))

    while stack:
        i, j, k = stack.pop()

        if i >= j:
            table[i][j] = [True, True]
        elif string[i] == string[j]:
            if table[i + 1][j - 1][1 if k > 0 else 0] is not None:
                table[i][j][1 if k > 0 else 0] = table[i + 1][j - 1][1 if k > 0 else 0]
            else:
                stack.append((i, j, k))
                stack.append((i + 1, j - 1, k))
                continue
        elif k > 0:
            result = None
            if table[i + 1][j][1 if k - 1 > 0 else 0] is not None:
                if table[i + 1][j][1 if k - 1 > 0 else 0]:
                    table[i][j][1 if k > 0 else 0] = True
                else:
                    if table[i][j - 1][1 if k - 1 > 0 else 0] is not None:
                        if table[i][j - 1][1 if k - 1 > 0 else 0]:
                            table[i][j][1 if k > 0 else 0] = True
                        else:
                            table[i][j][1 if k > 0 else 0] = False
                    else:
                        stack.append((i, j, k))
                        stack.append((i, j - 1, k - 1))
                        continue
            else:
                stack.append((i, j, k))
                stack.append((i + 1, j, k - 1))
                continue
    return any(table[0][len(string) - 1])


if __name__ == "__main__":
    print(can_be_palindrome(string='waterrfetawx', i=0, j=len('waterrfetawx') - 1, k=2))  # ANS = True
    print(can_be_palindrome_iterative2('apbax', 2))
    print(can_be_palindrome_iterative2('waterrfetawx', 2))
