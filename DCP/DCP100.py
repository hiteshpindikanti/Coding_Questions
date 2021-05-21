"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""


def get_moves_count(points: list) -> int:
    moves_count = 0
    for i in range(len(points) - 1):
        x_diff = abs(points[i][0] - points[i + 1][0])
        y_diff = abs(points[i][1] - points[i + 1][1])

        moves_count += min(x_diff, y_diff) + abs(x_diff - y_diff)
    return moves_count


if __name__ == "__main__":
    print(get_moves_count([(0, 0), (1, 1), (1, 2)]))
