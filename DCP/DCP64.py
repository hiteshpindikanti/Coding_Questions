"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""
from copy import deepcopy


def available_moves(position: tuple, n: int) -> list:
    moves = []
    row, col = position
    if row + 2 < n and col + 1 < n:
        moves.append((row + 2, col + 1))
    if row + 1 < n and col + 2 < n:
        moves.append((row + 1, col + 2))
    if row - 1 >= 0 and col + 2 < n:
        moves.append((row - 1, col + 2))
    if row - 2 >= 0 and col + 1 < n:
        moves.append((row - 2, col + 1))
    if row + 2 < n and col - 1 >= 0:
        moves.append((row + 2, col - 1))
    if row + 1 < n and col - 2 >= 0:
        moves.append((row + 1, col - 2))
    if row - 1 >= 0 and col - 2 >= 0:
        moves.append((row - 1, col - 2))
    if row - 2 >= 0 and col - 1 >= 0:
        moves.append((row - 2, col - 1))

    return moves


def count_knight_tours(n: int) -> int:
    total_squares = n*n
    count = 0
    # Stack in the form (visited, next_move)
    stack = [(set(), (row, col)) for col in range(n) for row in range(n)]
    while stack:
        visited, position = stack.pop(-1)
        visited.add(position)
        if len(visited) == total_squares:
            count += 1
        else:
            for next_position in available_moves(position, n):
                if next_position not in visited:
                    stack.append((deepcopy(visited), next_position))
    return count


print(count_knight_tours(2))
print(count_knight_tours(3))
print(count_knight_tours(4))
