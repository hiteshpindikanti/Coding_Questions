"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""


def pow(base: int, power: int) -> int:
    extra = 1
    while power > 1:
        if power % 2:
            extra *= base
            power -= 1
        base *= base
        power //= 2

    base *= extra

    return base


pow(2, 100)