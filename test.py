def list_n_rec(n) -> list:
    ans = []
    if n == 1:
        return [1]
    ans = list_n_rec(n - 1) + [n]
    return ans


def list_n_iterative(n) -> list:
    ans = [None] * n
    index = -1
    stack = [n]
    while stack:
        n = stack.pop(-1)
        if n == 1:
            pass
        else:
            stack.append(n - 1)
        ans[index] = n
        index -= 1

    return ans


def list_n(n):
    return list(range(1, n + 1))


import time

start = time.time()
list_n_iterative(10 ** 7)
end = time.time()
print("{} secs".format(end-start))

start = time.time()
list_n(10**7)
end = time.time()
print("{} secs".format(end-start))