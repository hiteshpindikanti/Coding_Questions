"""
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""


def to_be_removed_count(s: str) -> int:
    stack = []
    to_remove_count = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                to_remove_count += 1
    return to_remove_count + len(stack)


print(to_be_removed_count("()())()"))
print(to_be_removed_count(")("))
