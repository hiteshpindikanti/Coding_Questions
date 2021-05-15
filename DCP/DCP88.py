"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""


def quotient(num1: int, num2: int) -> int:
    num = num2
    q = 0
    while num <= num1:
        num += num2
        q += 1
    return q


print(quotient(10, 2))
