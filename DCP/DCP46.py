"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""
from copy import deepcopy


def get_longest_palindrom_substring(s: str) -> str:
    lps_length_table = [[1] * len(s) for _ in range(len(s))]
    lps = ""
    for row in range(len(s) - 1, -1, -1):
        for col in range(len(s) - 1, row, -1):
            if lps_length_table[row + 1][col - 1] == (col - 1) - (row + 1) + 1:
                # s[row+1:col] is a palindrome
                if s[row] == s[col]:
                    # s[row:col+1] is a palindrome
                    lps_length_table[row][col] = col - row + 1
                    if len(lps) < col - row + 1:
                        lps = s[row:col + 1]
                else:
                    lps_length_table[row][col] = lps_length_table[row + 1][col - 1]

    return lps


print(get_longest_palindrom_substring("aabcdcb"))
print(get_longest_palindrom_substring("bananas"))