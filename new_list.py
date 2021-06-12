class List(list):

    def __gt__(self, other):
        if isinstance(list, (list)):
            return list[::-1].__gt__(other[::-1])
        return super().__gt__(other)

    def __ge__(self, other):
        return list[::-1].__ge__(other[::-1])

    def __lt__(self, other):
        return list[::-1].__lt__(other[::-1])

    def __le__(self, other):
        return list[::-1].__le__(other[::-1])


if __name__ == "__main__":
    l1 = List()
    l1.append([1, 2])
    l2 = List()
    l2.append([2, 1])
    print(f'{l1[0]} > {l2[0]}')
    print(bool(l1[0] > l2[0]))
