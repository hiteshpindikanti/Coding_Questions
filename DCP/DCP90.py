"""
This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random


def generate_random(n: int, l: list) -> int:
    return random.choice(tuple(set(range(n)).difference(set(l))))


l = [1, 3, 5]
n = 3

print(generate_random(3, l))
