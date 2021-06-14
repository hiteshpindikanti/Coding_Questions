"""
This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""
import re


def is_number(string: str) -> bool:
    pattern = r'(-)?(\d)+((\.|e)?(\d)+)?'
    result = re.fullmatch(pattern, string)
    if result is None:
        return False
    else:
        return True


if __name__ == "__main__":
    # Positive examples
    print(is_number('10'))
    print(is_number('-10'))
    print(is_number('10.1'))
    print(is_number('-10.1'))
    print(is_number('1e5'))

    # Negative examples
    print(is_number('a'))
    print(is_number('x 1'))
    print(is_number('a -2'))
    print(is_number('-'))
