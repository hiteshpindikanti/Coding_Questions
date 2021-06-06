"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""
from collections import Counter, defaultdict


def is_count_match(original: dict, current: dict) -> bool:
    for key, val in original.items():
        if current[key] != val:
            return False
    return True


def get_anagram_indices(word: str, string: str) -> list:
    if len(word) > len(string):
        return []

    anagram_indices = []
    word_count = dict(Counter(word))
    current_count = defaultdict(int, Counter(string[:len(word)]))
    if is_count_match(word_count, current_count):
        anagram_indices.append(0)
    for i in range(len(string)-len(word)):
        current_count[string[i]] -= 1
        current_count[string[i+len(word)]] += 1
        if is_count_match(word_count, current_count):
            anagram_indices.append(i+1)
    return anagram_indices


if __name__ == "__main__":
    print(get_anagram_indices("ab", "abxaba"))
