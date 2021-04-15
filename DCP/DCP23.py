def bfs(m: list, start: tuple, end: tuple) -> int:
    queue = [(0, start)]
    visited = set()
    while queue:
        cost, position = queue.pop(0)
        visited.add(position)
        if position == end:
            return cost
        valid_next_positions = get_valid_moves(position=position, m=m)
        for next_position in valid_next_positions:
            if next_position not in visited:
                queue.append((cost + 1, next_position))


def get_valid_moves(position, m: list):
    x, y = position
    width = len(m[0])
    height = len(m)

    valid_positions = []
    if x - 1 >= 0 and not m[x - 1][y]:
        valid_positions.append((x - 1, y))
    if x + 1 < width and not m[x + 1][y]:
        valid_positions.append((x + 1, y))
    if y - 1 >= 0 and not m[x][y - 1]:
        valid_positions.append((x, y - 1))
    if y + 1 < height and not m[x][y + 1]:
        valid_positions.append((x, y + 1))
    return valid_positions


area = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]
s = (3, 0)
e = (0, 0)
print(bfs(m=area, start=s, end=e))
