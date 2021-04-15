def fun(s, dic: set):
    if s == "":
        return []
    for i in range(len(s) - 1, -1, -1):
        # print("Searching for : {}".format(s[i:]))
        if s[i:] in dic:
            lis = fun(s[:i], dic)
            if lis is not None:
                return lis + [s[i:]]
    else:
        return None


string = 'thequickbrownfox'
dic_set = {'quick', 'brown', 'the', 'fox'}
print(fun(string, dic_set))

string = 'bedbathandbeyond'
dic_set = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
print(fun(string, dic_set))
