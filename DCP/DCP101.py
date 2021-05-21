"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""
import math


def prime_number():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


def is_prime(num) -> bool:
    if num == 2:
        return True
    if not num & 1:
        return False
    for divisor in range(3, int(num ** 0.5), 2):
        ans = num / divisor
        if not ans - math.floor(ans):
            return False
    return True


def get_pair(num) -> tuple:
    prime_generator = prime_number()
    prime = next(prime_generator)
    while prime < num:
        if is_prime(num - prime):
            return prime, num - prime
        prime = next(prime_generator)
    return None, None


if __name__ == "__main__":
    for number in range(4, 200, 2):
        print("{} : {}".format(number, get_pair(number)))