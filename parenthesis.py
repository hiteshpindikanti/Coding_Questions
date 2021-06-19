def generate_parenthesis(num: int) -> set:
    if num == 1:
        return {"()"}
    parenthesis = set()
    sub_parenthesis = generate_parenthesis(num - 1)
    parenthesis.update(set(map(lambda x: "()" + x, sub_parenthesis)))
    parenthesis.update(set(map(lambda x: "(" + x + ")", sub_parenthesis)))
    parenthesis.update(set(map(lambda x: x + "()", sub_parenthesis)))
    return parenthesis


if __name__ == "__main__":
    print(generate_parenthesis(3))
    i: int = 0
    lst: list[int] = [1, 2, 3, 4]
