def next_num(num: int) -> tuple:
    return smallest_next_num(num), largest_next_num(num)


def smallest_next_num(num: int) -> int:
    num_cpy = num
    count = 0
    while num > 0 and num & 1 == 0:
        count += 1
        num >>= 1
    remove = count
    count += 1
    num >>= 1
    while num > 0 and num & 1 == 1:
        count += 1
        num >>= 1
    add = count
    return (num_cpy & ~(1 << remove)) | (1 << add)


def largest_next_num(num: int) -> int:
    zeros = 0
    ones = 0
    while num > 0:
        if num & 1 == 0:
            zeros += 1
        else:
            ones += 1
        num >>= 1

    return (2 ** (zeros + ones) - 1) & ~(2 ** zeros - 1)


n = 9
print("num = {0:b}\nsmallest_next_num = {1:b}\nlargest_next_num = {2:b}".format(n, *next_num(n)))
