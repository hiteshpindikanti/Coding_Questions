def get_trapped_water(buildings: list) -> int:
    index, max_height = get_max(buildings)
    trapped_water = 0

    # First Half
    height = buildings[0]
    for i in range(1, index):
        height = max(height, buildings[i])
        trapped_water += height - buildings[i]

    # Second Half
    height = buildings[-1]
    for i in range(len(buildings) - 2, index, -1):
        height = max(height, buildings[i])
        trapped_water += height - buildings[i]

    return trapped_water


def get_max(arr: list) -> tuple:
    max_i = 0
    max_val = 0
    for i, val in enumerate(arr):
        if val > max_val:
            max_val = val
            max_i = i
    return max_i, max_val


print(get_trapped_water([2, 1, 2]))
print(get_trapped_water([3, 0, 1, 3, 0, 5]))
print(get_trapped_water([5, 4, 1, 2]))
