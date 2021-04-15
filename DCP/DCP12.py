# Input
s = "ab"
k = 1

i, j = 0, 0
d = {s[i]: 1}
max_length = 1
while j < len(s) - 1:
    if s[j + 1] in d.keys():
        j += 1
        d[s[j]] += 1
        max_length = max(max_length, j - i + 1)
    elif len(d.keys()) < k:
        j += 1
        d[s[j]] = 1
    else:
        while len(d.keys()) == k:
            d[s[i]] -= 1
            i += 1
            if d[s[i - 1]] == 0:
                d.pop(s[i - 1])

print(max_length)
