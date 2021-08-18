from copy import deepcopy


def found_in_grid(grid: list[list[str]], word: str) -> bool:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                if search_grid(row, col, word, grid):
                    return True
    return False


def search_grid(start_row, start_col, word, grid) -> bool:
    stack = [[(None, None), (start_row, start_col)]]
    while stack:
        current_path = stack.pop()
        if len(current_path)-1 == len(word):
            return True
        row, col = current_path[-1]
        current_path_set = set(current_path)
        for adjacent_node in get_adjacent_nodes(row, col, len(grid), len(grid[0])):
            if adjacent_node not in current_path_set and grid[adjacent_node[0]][adjacent_node[1]] == word[len(current_path) - 1]:
                path = deepcopy(current_path)
                path.append(adjacent_node)
                stack.append(path)
    return False


def get_adjacent_nodes(row, col, n_rows, n_cols) -> list[tuple]:
    adjacent_nodes = set()
    if row > 0:
        adjacent_nodes.add((row - 1, col))
        if col > 0:
            adjacent_nodes.add((row, col - 1))
        if col < n_cols - 1:
            adjacent_nodes.add((row, col + 1))
    if row < n_rows - 1:
        adjacent_nodes.add((row + 1, col))
    return adjacent_nodes


if __name__ == "__main__":
    grid_ = [['A', 'B', 'C'],
             ['B', 'A', 'C'],
             ['C', 'B', 'A']]
    print(found_in_grid(grid_, "ABABA"))   # True
    print(found_in_grid(grid_, "ABCBA"))  # True
    print(found_in_grid(grid_, "BCBC"))  # False
