def justify(words: list, k: int) -> list:
    words.append('.')
    n = len(words)
    i = 0
    justified_words = []
    while i < n-1:
        current_line = 0
        spaces = 0
        sentence = []
        while i < n and current_line < k + 1:
            sentence.append(words[i])
            spaces += 1
            current_line += len(words[i]) + 1
            i += 1
        else:
            current_line -= len(sentence.pop(-1)) + 2
            spaces -= 2
            i -= 1

        fixed_spaces = (k - current_line) // spaces
        extra_spaces = (k - current_line) % spaces
        s = ""
        for word in sentence:
            s += word + " " * (1 + fixed_spaces + (1 if extra_spaces > 0 else 0))
            extra_spaces -= 1
        justified_words.append(s.strip())
    return justified_words


words_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
line_length = 16
print(justify(words_list, line_length))
