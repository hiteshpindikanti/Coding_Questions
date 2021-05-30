"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def can_be_shifted(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in s1 * 2


if __name__ == "__main__":
    print(can_be_shifted('abcde', 'cdeab'))
    print(can_be_shifted('abc', 'acb'))
