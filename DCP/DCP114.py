"""
This problem was asked by Facebook.

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""
from re import split as rex_split
from typing import FrozenSet


def reverse(string: str) -> str:
    acceptable_delimiters = frozenset({'\\', '/', '*', ';', ':', ' '})

    # Split the string into list of words
    arr = list(filter(lambda x: x != '', rex_split('[ \\\*;/:]', string)))

    # Collect the delimiters in their order
    delimiters = []
    i = 0
    while i < len(string):
        j = i
        while j < len(string) and string[j] in acceptable_delimiters:
            j += 1
        if i == j:
            i += 1
        else:
            delimiters.append(string[i:j])
            i = j

    # Reverse the order of words
    last_index = len(arr) - 1
    for i in range(len(arr) // 2):
        arr[i], arr[last_index - i] = arr[last_index - i], arr[i]

    # Join the array and delimiters to form the final answer
    final_string_list = []
    delimiter_index = 0
    arr_index = 0
    if string[0] in acceptable_delimiters:
        final_string_list.append(string[0])
        delimiter_index += 1
    while delimiter_index < len(delimiters) and arr_index < len(arr):
        final_string_list.append(arr[arr_index] + delimiters[delimiter_index])
        arr_index += 1
        delimiter_index += 1
    if arr_index < len(arr):
        final_string_list.append(arr[arr_index])

    # Return the final string
    return ''.join(final_string_list)


if __name__ == "__main__":
    print(reverse("hello/world:here"))  # ANS = "here/world:hello"
    print(reverse("hello/world:here/"))  # ANS = "here/world:hello/"
    print(reverse("hello//world:here"))  # ANS = "here//world:hello"
