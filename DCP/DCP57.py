"""
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""


def break_up(s: str, k: int) -> list:
    words = s.split(" ")
    result = []
    i = 1
    line = words[0]
    while i < len(words):
        line_copy = line
        line += " " + words[i]
        if len(line) > k:
            result.append(line_copy)
            line = words[i]
        elif len(line) == k:
            result.append(line)
            i += 1
            line = words[i]

        i += 1
    else:
        if line:
            result.append(line)
    return result


sentence = "the quick brown fox jumps over the lazy dog"
print(break_up(sentence, k=10))
