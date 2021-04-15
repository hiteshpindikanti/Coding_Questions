from collections import Counter


def segregate_rgb(l: list):
    count = Counter(l)
    r = 0
    g = count['R']
    b = g + count['G']
    r_limit = g
    g_limit = b
    b_limit = len(l)

    while r < r_limit or g < g_limit or b < b_limit:
        while r < r_limit and l[r] == 'R':
            r += 1
        while g < g_limit and l[g] == 'G':
            g += 1
        while b < b_limit and l[b] == 'B':
            b += 1
        if r < r_limit and b < b_limit and l[r] == 'B' and l[b] == 'R':
            l[r], l[b] = l[b], l[r]
        elif r < r_limit and g < g_limit and l[r] == 'G' and l[g] == 'R':
            l[r], l[g] = l[g], l[r]
        elif g < g_limit and b < b_limit and l[g] == 'B' and l[b] == 'G':
            l[g], l[b] = l[b], l[g]
        elif r < r_limit and b < b_limit and g < g_limit:
            if l[r] == 'B':
                l[r], l[b], l[g] = l[g], l[r], l[b]
            elif l[r] == 'G':
                l[r], l[b], l[g] = l[b], l[g], l[r]


arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(arr)
segregate_rgb(arr)
print(arr)
