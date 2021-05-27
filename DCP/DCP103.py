"""
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
from queue import Queue
from collections import defaultdict


def get_substring(s: str, chars: set) -> str:
    substring = Queue()
    min_substring = list(map(str, s))
    start = 0
    while s[start] not in chars:
        start += 1
    end = start
    substring.put(s[start])
    substring_chars_counter = defaultdict(int)
    substring_chars_counter[s[start]] += 1
    while True:

        while chars.difference(substring_chars_counter.keys()):
            end += 1
            if end < len(s):
                substring_chars_counter[s[end]] += 1
                substring.put(s[end])
            else:
                break

        if end == len(s):
            break

        while not chars.difference(substring_chars_counter.keys()):
            if substring.qsize() < len(min_substring):
                min_substring = list(substring.queue)

            substring.get()
            substring_chars_counter[s[start]] -= 1
            if not substring_chars_counter[s[start]]:
                substring_chars_counter.pop(s[start])
            if start == end:
                break
            start += 1
        else:

            continue

        break

    return ''.join(min_substring)


if __name__ == "__main__":
    print(get_substring("figehaeci", {'a', 'e', 'i'}))
