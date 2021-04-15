def encode(s: str) -> str:
    count = 1
    encoded_str = ""
    for i in range(1, len(s)):
        if i == len(s) - 1:
            if s[i - 1] == s[i]:
                count += 1
            encoded_str += str(count) + s[i]

        if s[i - 1] == s[i]:
            count += 1
        else:
            encoded_str += str(count) + s[i - 1]
            count = 1
    return encoded_str


def decode(s: str) -> str:
    decoded_str = ""
    for i in range(0, len(s), 2):
        count = int(s[i])
        decoded_str += s[i + 1] * count
    return decoded_str


message = "AAAABBBCCDAA"
print(message)
print(encode(message))
print(decode(encode(message)))
