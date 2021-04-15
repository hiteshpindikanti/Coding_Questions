def get_power_set(s: set) -> set:
    power_set = {frozenset()}
    length = 0
    while len(power_set) > length:
        length = len(power_set)
        temp_set = set()
        for e in power_set:

            for i in s:
                temp_set.add(frozenset(e.union({i})))
        power_set.update(temp_set)
    return power_set


print(get_power_set({1, 2, 3}))
