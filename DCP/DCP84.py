"""
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def get_adjacent_coordinates(matrix, coordinates) -> list:
    max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1
    row, col = coordinates

    adjacent_coordinates = set()
    if row > 0:
        adjacent_coordinates.add((row - 1, col))
        if col > 0:
            adjacent_coordinates.add((row, col - 1))
            adjacent_coordinates.add((row - 1, col - 1))
        if col < max_col:
            adjacent_coordinates.add((row, col + 1))
            adjacent_coordinates.add((row - 1, col + 1))
    if row < max_row:
        adjacent_coordinates.add((row + 1, col))
        if col > 0:
            adjacent_coordinates.add((row, col - 1))
            adjacent_coordinates.add((row + 1, col - 1))
        if col < max_col:
            adjacent_coordinates.add((row, col + 1))
            adjacent_coordinates.add((row + 1, col + 1))
    filtered_adjacent_coordinates = []
    for coordinates in adjacent_coordinates:
        if matrix[coordinates[0]][coordinates[1]] == 1:
            filtered_adjacent_coordinates.append(coordinates)

    return filtered_adjacent_coordinates


def get_island_count(matrix: list) -> int:
    visited = set()
    island_count = 0

    while True:
        # Get next island's starting coordinates
        row_index, col_index = -1, -1
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                if col == 1 and (row_index, col_index) not in visited:
                    break
            else:
                continue
            break
        else:
            return island_count

        visited.add((row_index, col_index))
        stack = [(row_index, col_index)]
        while stack:
            row_index, col_index = stack.pop(-1)
            for adjacent_coordinates in get_adjacent_coordinates(matrix, (row_index, col_index)):
                if adjacent_coordinates not in visited:
                    visited.add(adjacent_coordinates)
                    stack.append(adjacent_coordinates)

        island_count += 1


mat = [[1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 0, 1],
       [1, 1, 0, 0, 1]]

print(get_island_count(mat))
