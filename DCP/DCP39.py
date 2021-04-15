import numpy as np


def get_state(old_alive_cells: set, time: int) -> list:
    for _ in range(time):
        check_coordinates = set()
        for x, y in old_alive_cells:
            check_coordinates.update(get_adjacent_cells(x, y))
        check_coordinates.update(old_alive_cells)

        new_alive_cells = set()
        for x, y in check_coordinates:
            alive_adjacent_cells_count = num_alive_adjacent_cells(x, y, old_alive_cells)
            if (x, y) in old_alive_cells:
                if alive_adjacent_cells_count in {2, 3}:
                    new_alive_cells.add((x, y))
            else:
                if alive_adjacent_cells_count == 3:
                    new_alive_cells.add((x, y))

        old_alive_cells = new_alive_cells

    return make_board(old_alive_cells)


def get_adjacent_cells(x, y) -> list:
    adjacent_cells = [(x, y + 1), (x + 1, y), (x + 1, y + 1)]
    if x > 0:
        adjacent_cells.append((x - 1, y))
        adjacent_cells.append((x - 1, y + 1))
    if y > 0:
        adjacent_cells.append((x, y - 1))
        adjacent_cells.append((x + 1, y - 1))
    if x > 0 and y > 0:
        adjacent_cells.append((x - 1, y - 1))

    return adjacent_cells


def num_alive_adjacent_cells(x, y, alive_cells: set) -> int:
    adjacent_cells = get_adjacent_cells(x, y)
    adjacent_alive_cells_count = 0
    for cell in adjacent_cells:
        if cell in alive_cells:
            adjacent_alive_cells_count += 1

    return adjacent_alive_cells_count


def make_board(alive_cells) -> list:
    if not alive_cells:
        return []
    x_min, y_min = float('inf'), float('inf')
    x_max, y_max = 0, 0

    for x, y in alive_cells:
        x_min = min(x, x_min)
        y_min = min(y, y_min)
        x_max = max(x, x_max)
        y_max = max(y, y_max)

    print("{},{},{},{}".format(x_min, y_min, x_max, y_max))
    print("alive_cells = {}".format(alive_cells))
    board = [['.'] * (y_max - y_min + 1) for _ in range(x_max - x_min + 1)]
    for x, y in alive_cells:
        board[x - x_min][y - y_min] = '*'

    return board


print(np.array(get_state({(1, 0), (0, 1), (1, 1)}, 1)))
