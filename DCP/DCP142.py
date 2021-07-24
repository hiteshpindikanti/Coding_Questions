"""
This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""


# Recursive solution O(3^n)
def is_balanced_recursive(string: str, stack_count: int = 0) -> bool:
    for i in range(len(string)):
        if string[i] == "(":
            stack_count += 1
        elif string[i] == ")":
            if stack_count:
                stack_count -= 1
            else:
                return False
        elif string[i] == "*":
            return is_balanced_recursive(string[i + 1:], stack_count) or \
                   is_balanced_recursive(string[i + 1:], stack_count + 1) or \
                   (is_balanced_recursive(string[i + 1:], stack_count - 1) if stack_count else False)
    return True


# Alternative solution O(n)
def is_balanced(string) -> bool:
    low = 0
    high = 0
    for ch in string:
        if ch == "(":
            low += 1
            high += 1
        elif ch == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        if low <= high <= 0:
            return False

    return True


if __name__ == "__main__":
    assert is_balanced("(()*") is True
    assert is_balanced("(*)") is True
    assert is_balanced(")*(") is False
    assert is_balanced("*"*100000) is True
