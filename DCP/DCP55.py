"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""
from collections import defaultdict


class URL:
    def __init__(self):
        self.dict = defaultdict(set)

    def __to_char(self, val: int) -> str:
        if 0 <= val <= 9:
            return str(val)
        elif 10 <= val <= 35:
            return chr(val - 10 + ord('a'))
        elif 36 <= val <= 61:
            return chr(val - 36 + ord('A'))

    def shorten(self, url: str) -> str:

        block_size = len(url) // 6
        i = 0
        j = block_size + 1
        result = []
        while j <= len(url):
            result.append(self.__to_char(sum(map(ord, url[i:j])) % 62))
            i = j
            j = j + block_size
        key = ''.join(result)
        self.dict[key].add(url)
        return key

    def restore(self, key: str):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return None


if __name__ == "__main__":
    obj = URL()
    ans = obj.shorten(
        "https://answers.microsoft.com/en-us/msoffice/forum/msoffice_word-mso_other-mso_365hp/create-a-4x4-matrix-in-word/556be599-110d-4363-8615-c7c9dd2dc9d4")
    print(ans)
    print(obj.restore(ans))
