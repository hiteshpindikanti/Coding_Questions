def longest_k_interspace_substring(word: str, k: int) -> str:
    if len(word) == 1:
        return word
    start = 0
    end = 1
    substring_index = (0, 0)
    while start < end < len(word):
        while end<len(word) and abs(ord(word[end-1]) - ord(word[end])) <= k:
            end += 1
        if end-start > (substring_index[1]-substring_index[0]):
            substring_index = (start, end)
        start = end
        end += 1
    return word[substring_index[0]: substring_index[1]]


if __name__ == "__main__":
    print(longest_k_interspace_substring("wedding", 0))  # dd
    print(longest_k_interspace_substring("ababbacaabbbb", 1))  # ababba
    print(longest_k_interspace_substring("hackerrank", 0))  # rr
    print(longest_k_interspace_substring("az", 1))  # a




