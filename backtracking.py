from typing import List, Set, Dict


def get_all_sequences(word: str) -> list[str]:
    all_sequences = []
    for length in range(1, len(word) + 1):
        all_sequences.extend(get_all_sequences_len_k(word, length))
    return all_sequences


def get_all_sequences_len_k(word: str, k: int) -> list[str]:
    if not k:
        return [""]
    all_sequences_len_k = []
    seen = set()
    for index, ch in enumerate(word):
        if ch not in seen:
            seen.add(ch)
            remaining_word = word[:index] + word[index + 1:]
            remaining_seq = get_all_sequences_len_k(remaining_word, k - 1)
            all_sequences_len_k.extend(list(map(lambda x: ch + x, remaining_seq)))
    return all_sequences_len_k


if __name__ == "__main__":
    print(get_all_sequences("aab"))
    print(get_all_sequences("abc"))
