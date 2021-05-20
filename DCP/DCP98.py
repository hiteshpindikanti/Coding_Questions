"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

"""


def get_adjacent_cells(coordinates: tuple, board_height: int, board_width: int) -> set:
    row, col = coordinates
    adjacent_cells = set()
    if row > 0:
        adjacent_cells.add((row - 1, col))
        if col > 0:
            adjacent_cells.add((row, col - 1))
        if col < board_width - 1:
            adjacent_cells.add((row, col + 1))
    if row < board_height - 1:
        adjacent_cells.add((row + 1, col))
        if col > 0:
            adjacent_cells.add((row, col - 1))
        if col < board_width - 1:
            adjacent_cells.add((row, col + 1))
    return adjacent_cells


def exists(board: list, word: str) -> bool:
    board_height = len(board)
    board_width = len(board[0])
    stack = []
    for row in range(board_height):
        for col in range(board_width):
            if board[row][col] == word[0]:
                stack.append([(row, col)])

    while stack:
        current_path = stack.pop(-1)
        current_path_set = set(current_path)
        adjacent_cells = get_adjacent_cells(current_path[-1], board_height, board_width)
        
        for row, col in adjacent_cells:
            if (row, col) not in current_path_set and board[row][col] == word[len(current_path)]:
                if len(current_path) == len(word) - 1:
                    return True
                stack.append(current_path + [(row, col)])

    return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(exists(board, "ABCCED"))  # returns true
    print(exists(board, "SEE"))  # returns true
    print(exists(board, "ABCB"))  # returns false.
