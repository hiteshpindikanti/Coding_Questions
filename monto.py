import random


def game():
    a, b, r, e = (0, 0, 0, 0)
    while r <= 7:
        e += int(a == b != 0)
        if random.randint(0, 1):
            a += 1
        else:
            b += 1
        r += 1
    return {"rounds": r, "equal": e, "winner": ('a' if a > b else 'b')}

if __name__ == "__main__":
    res = {}
    g1 = game()
    res["roundsTotal"] = g1["rounds"]
    res["roundsMin"] = g1["rounds"]
    res["roundsMax"] = g1["rounds"]
    res["equalsTotal"] = g1["equal"]
    res["eqaulMin"] = g1["equal"]
    res["equalMax"] = g1["equal"]
    res["awins"] = int(g1["winner"] == 'a')
    res["bwins"] = int(g1["winner"] == 'b')
    for i in range(10 ** 6 - 1):
        g = game()
        res["roundsTotal"] += g["rounds"]
        res["roundsMin"] = min(g["rounds"], res["roundsMin"])
        res["roundsMax"] = max(g["rounds"], res["roundsMax"])
        res["equalsTotal"] += g["equal"]
        res["eqaulMin"] = min(g["equal"], res["eqaulMin"])
        res["equalMax"] = max(g["equal"], res["equalMax"])
        res["awins"] += int(g["winner"] == 'a')
        res["bwins"] += int(g["winner"] == 'b')
    res["roundsAvg"] = res["roundsTotal"] / 10 ** 6
    res["equalAvg"] = res["equalsTotal"] / 10 ** 6
    for k, v in res.items():
        print(k, v)