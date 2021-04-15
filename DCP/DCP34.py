def get_palindrome_string(s: str) -> str:
    if s[0] > s[-1]:
        s = s[::-1]
    stack = []
    for ch in s:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop(-1)
    return s + ''.join(stack[::-1])


print(get_palindrome_string("race"))
print(get_palindrome_string("google"))
