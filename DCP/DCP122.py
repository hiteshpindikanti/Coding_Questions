"""
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


# Recursive
def get_max_coins(matrix: list[list[int]], start: tuple = (0, 0)) -> int:
    coins = matrix[start[0]][start[1]]
    matrix_length = len(matrix)
    matrix_width = len(matrix[0])

    sub_coins1 = sub_coins2 = 0

    # Going Right
    if start[1] + 1 < matrix_width:
        sub_coins1 = get_max_coins(matrix, (start[0], start[1] + 1))

    # Going Down
    if start[0] + 1 < matrix_length:
        sub_coins2 = get_max_coins(matrix, (start[0] + 1, start[1]))

    coins += max(sub_coins1, sub_coins2)
    return coins


# Iterative DP
def get_max_coins_iterative(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    matrix_length = len(matrix)
    matrix_width = len(matrix[0])

    for row in range(matrix_length - 1, -1, -1):
        for column in range(matrix_width - 1, -1, -1):
            possible_max_coins = []
            if row + 1 < matrix_length:
                possible_max_coins.append(matrix[row + 1][column])
            if column + 1 < matrix_width:
                possible_max_coins.append(matrix[row][column + 1])

            if possible_max_coins:
                matrix[row][column] += max(possible_max_coins)

    return matrix[0][0]


if __name__ == "__main__":
    game_map = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1],
    ]
    print(get_max_coins_iterative(game_map))
