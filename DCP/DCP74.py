"""
This problem was asked by Apple.
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.
For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 4 | 6 | 8 | 10 | 12 |
| 3 | 6 | 9 | 12 | 15 | 18 |
| 4 | 8 | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""
from collections import defaultdict
from copy import deepcopy


def prime_number():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


def prime_factorization(num: int) -> dict:
    factors = defaultdict(int)
    prime_num = prime_number()
    while num > 1:
        prime = next(prime_num)
        while num % prime == 0:
            num //= prime
            factors[prime] += 1
    return factors


def two_factors(factors, num1: int, num2: int = 1) -> set:
    ans = {frozenset({num1, num2})}
    for key in factors.keys():
        if factors[key] > 0:
            d1 = deepcopy(factors)
            d1[key] -= 1
            if d1[key] == 0:
                d1.pop(key)
            ans.update(two_factors(d1, num1 // key, num2 * key))

    return ans


def appearance_count(n: int, x: int) -> int:
    factors = two_factors(prime_factorization(x), x)
    count = 0
    for factor1, factor2 in factors:
        if factor1 <= n and factor2 <= n:
            count += 1 if factor1 == factor2 else 2
    return count


print(appearance_count(6, 12))
