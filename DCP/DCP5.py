def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair) -> int:
    return pair(lambda x, y: x)


def cdr(pair) -> int:
    return pair(lambda x, y: y)


print(cdr(cons(2, 5)))
