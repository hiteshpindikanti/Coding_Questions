import bisect


def comb_sum(l: list, target: int) -> list:
    print("list = {}, target = {}".format(l, target))

    if target == 0:
        print("returning: {}".format([[]]))
        return [[]]
    elif target < 0 or not l:
        print("returning: {}".format(None))
        return None

    i = 0
    result = []

    r = comb_sum(l, target - l[-1])
    if r is not None:
        result.extend(list(map(lambda x: [l[-1]] + x, r)))

    r = comb_sum(l[:-1], target - i * l[-1])
    if r is not None:
        result.extend(list(map(lambda x: [i * l[-1]] if i != 0 else [] + x, r)))

    print("returning: {}".format(result))
    return result


if __name__ == "__main__":
    candidates = [1]
    target = 1
    candidates.sort()
    index = bisect.bisect(candidates, target)
    print(comb_sum(candidates[:index+1], target))
