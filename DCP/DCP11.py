from collections import defaultdict

dictionary = defaultdict(list)
with open("../LeetCode/words_alpha.txt") as file:
    for word in file.read().split():
        for i in range(1, len(word)-1):
            dictionary[word[:i]].append(word)

print(dictionary['part'][:10])