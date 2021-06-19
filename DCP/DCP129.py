"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""


# Binary search approach
def get_square_root(n, precision: int = 5):
    lower_limit = 0.0
    higher_limit = n
    precision = 10 ** (-precision)
    square_root = (lower_limit + higher_limit) / 2
    error = square_root * square_root - n
    while abs(error) > precision:
        if error > 0:
            higher_limit = square_root
        else:
            lower_limit = square_root
        square_root = (lower_limit + higher_limit) / 2
        error = square_root * square_root - n
    return square_root


if __name__ == "__main__":
    print(get_square_root(9))
