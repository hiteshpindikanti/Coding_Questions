"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""
from copy import deepcopy


class SudokuSolver:
    def __init__(self, board: list):
        pass

    @staticmethod
    def __satisfy_constrains(domain):
        for row in range(9):
            for col in range(9):
                if len(domain[row][col]) == 1:
                    value = next(iter(domain[row][col]))

                    # process current row constraints
                    for i in range(9):
                        if i != col:
                            if value in domain[row][i]:
                                domain[row][i].remove(value)

                    # process current col constraints
                    for i in range(9):
                        if i != row:
                            if value in domain[i][col]:
                                domain[i][col].remove(value)

                    # process current block constraints
                    block_row = (row // 3) * 3
                    block_col = (col // 3) * 3

                    for i in range(block_row, block_row + 3):
                        for j in range(block_col, block_col + 3):
                            if i != row and j != col:
                                if value in domain[i][j]:
                                    domain[i][j].remove(value)

    @staticmethod
    def __best_assignment_order(domain) -> list:
        assignment_order = []
        for row in range(9):
            for col in range(9):
                assignment_order.append((len(domain[row][col]), row, col))
        assignment_order = sorted(filter(lambda x: x[0] != 1, assignment_order))
        return assignment_order

    @staticmethod
    def __check_board(domain) -> str:
        solved_flag = True
        for row in range(9):
            for col in range(9):
                if len(domain[row][col]) == 0:
                    return "UNSOLVABLE"
                elif len(domain[row][col]) > 1:
                    solved_flag = False
        if solved_flag:
            return "SOLVED"
        else:
            return "CONTINUE"
        pass

    @staticmethod
    def solve(board) -> list:

        domain = [[{i for i in range(1, 10)} for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    domain[row][col] = {board[row][col]}

        # [print("INITIAL:")] + [print(line) for line in domain]

        stack = [deepcopy(domain)]
        while stack:
            domain = stack.pop(-1)
            SudokuSolver.__satisfy_constrains(domain)
            status = SudokuSolver.__check_board(domain)
            if status == "SOLVED":
                return domain
                # return [[next(iter(domain[row][col])) for col in range(9)] for row in range(9)]

            elif status == "UNSOLVABLE":
                continue
            else:
                for _, row, col in SudokuSolver.__best_assignment_order(domain):
                    temp = domain[row][col]
                    for val in temp:
                        domain[row][col] = {val}
                        stack.append(deepcopy(domain))
                    domain[row][col] = temp
        return domain


if __name__ == "__main__":
    # sudoku = list(map(lambda x: list(map(lambda x: int(x) if x else 0, x.split("\t"))), b.split("\n")))

    sudoku = [[0, 9, 0, 4, 0, 1, 7, 0, 0],
              [6, 1, 2, 0, 7, 8, 0, 0, 0],
              [8, 0, 4, 5, 0, 2, 1, 0, 0],
              [0, 4, 0, 0, 0, 0, 0, 0, 8],
              [0, 8, 0, 3, 0, 0, 6, 0, 0],
              [2, 3, 0, 8, 0, 0, 0, 5, 0],
              [4, 5, 0, 1, 8, 0, 2, 6, 7],
              [0, 0, 8, 0, 5, 0, 0, 3, 9],
              [0, 0, 0, 0, 0, 4, 8, 1, 0]]

    for line in SudokuSolver.solve(sudoku):
        print(line)
