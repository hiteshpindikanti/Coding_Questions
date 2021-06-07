"""
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse(string: str) -> str:
    arr = string.split(" ")
    last_index = len(arr) - 1
    for i in range(len(arr) // 2):
        arr[i], arr[last_index - i] = arr[last_index - i], arr[i]

    return ' '.join(arr)


if __name__ == "__main__":
    print(reverse("hello world here"))
