"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def perfect_number(n: int) -> int:
    num = 19
    for _ in range(n - 1):
        digit_len = len(str(num))
        i = 1
        while num % i == 0:
            i *= 10

        remaining_digit = ((num // (i // 10)) % 10) - 1
        num = ((num // i) + 1) * i + remaining_digit

        if len(str(num)) > digit_len:
            num += 9

    return num


for i in range(1, 111):
    print(perfect_number(i))
