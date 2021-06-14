def get_numbers():
    num = 0
    yield num
    num += 1


if __name__ == "__main__":
    number = get_numbers()
    for i in number:
        print(i)

    # print(next(number))
    # print(next(number))
    # print(next(number))
    # print(next(number))
    # print(next(number))

