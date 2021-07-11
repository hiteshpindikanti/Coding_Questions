"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""


def get_largest_rectangle_area(matrix: list[list[int]]) -> int:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    visited = [[False] * n_cols for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            if not visited[row][col]:
                if matrix[row][col] == 0:
                    visited[row][col] = True
                else:
                    get_area_of_cluster(matrix, visited, row, col)

    pass


def get_area_of_cluster(matrix: list[list[int]], visited: list[list[bool]], initial_row_index: int,
                        initial_col_index: int) -> int:
    stack = [(initial_row_index, initial_col_index)]
    while stack:
        pass


if __name__ == "__main__":
    play = [[1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 0]]

    print(get_largest_rectangle_area(play))
