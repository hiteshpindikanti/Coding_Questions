mapping = {ch - 96: chr(ch) for ch in range(97, 97 + 26)}


def decoding(msg: str, start: int = 0) -> list:
    print("start = {}".format(start))
    if start == len(msg)-1:
        return [[mapping[int(msg[start])]]]
    elif start > len(msg)-1:
        return [[]]
    else:
        decoded_msgs = []
        decoded_msgs.extend(list(map(lambda x: [mapping[int(msg[start])]]+x, decoding(msg, start=start+1))))
        if int(msg[start:start+2]) <= 26:
            decoded_msgs.extend(list(map(lambda x: [mapping[int(msg[start:start+2])]]+x,
                                         decoding(msg, start=start+2))))

        return decoded_msgs


print(decoding("1126"))