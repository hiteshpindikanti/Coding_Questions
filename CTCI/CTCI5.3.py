import time
import math


def flip_to_win_bit(num: int) -> int:
    before = 0
    max_len = before + 1
    while num > 0:
        after = 0
        num >>= 1
        while num & 1 == 1:
            after += 1
            num >>= 1
        max_len = max(max_len, before + after + 1)
        before = after
    return max_len


def flip_to_win_bit2(num: int) -> int:
    before = 0
    i = 0
    max_len = before + 1
    digits = math.log2(num)
    while i < digits:
        after = 0
        i += 1
        while num & (1 << i) == 1:
            after += 1
            i += 1
        max_len = max(max_len, before + after + 1)
        before = after
    return max_len


def flip_to_win_normal(num: int) -> int:
    s = bin(num)
    i = len(s) - 1
    before = 0
    max_len = before+1
    while i > 1:
        i -= 1
        after = 0
        while s[i] == '1':
            after += 1
            i -= 1
        max_len = max(max_len, before + after + 1)
        before = after
    return max_len


n = 2 ** 10 ** 6

start = time.time()
ans = flip_to_win_bit(n - 1)
end = time.time()
print("flip_to_win_bit = {}, time = {}".format(ans, end - start))

start = time.time()
ans = flip_to_win_normal(n - 1)
end = time.time()
print("flip_to_win_normal = {}, time = {}".format(ans, end - start))
