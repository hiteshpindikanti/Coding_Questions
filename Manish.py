def is_divisible(s: str, t: str) -> bool:
    if len(s) % len(t) != 0:
        return False
    i = 0
    for ch in s:
        if t[i] != ch:
            return False
        i = (i + 1) % len(t)
    return True


def get_min_str_len(s: str, t: str):
    if is_divisible(s, t):
        min_str_len = len(t)
        for i in range(1, len(t)):
            if is_divisible(t, t[:i]):
                min_str_len = min(min_str_len, i)

        return min_str_len
    else:
        return -1


if __name__ == "__main__":
    print(get_min_str_len("abababab", "abab"))
    print(get_min_str_len("ababa", "ab"))
    print(get_min_str_len("rbrb", "rbrb"))
    print(get_min_str_len("lrbblrbb", "lrbb"))
    print(get_min_str_len("bcdbcdbcdbcd", "bcdbcd"))
    print(get_min_str_len("bcdbcdbcd", "bcdbcd"))

