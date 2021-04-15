def bins(num, bits:int=32) -> str:
    return bin(num & 2**(bits+1)-1)


def insert_into(M, N, i, j) -> int:
    left = ~((1 << j+1) - 1)
    right = ((1 << i) - 1)
    mask = left | right
    modified_M = M & mask
    modified_N = N << i
    print("left = {}\nright = {}\nmask = {}\nmodified_N = {}\nmodified_M = {}"
          .format(bins(left), bins(right), bins(mask), bins(modified_N), bins(modified_M)))
    return modified_N | modified_M


M = 1024
N = 10
i = 3
j = 6

print("M = {0:b}".format(M))
print("N = {0:b}".format(N))
print("j = {}, i = {}".format(j, i))
ans = insert_into(M, N, i, j)
print("ans = {0:b}".format(ans))
