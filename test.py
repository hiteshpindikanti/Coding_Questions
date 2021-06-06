
def fib(num: int):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return fib(num - 1) + fib(num - 2)


def fib_list(num: int) -> list:
    if num == 1:
        return [0, 1]

    result = fib_list(num - 1)
    result.append(result[-1] + result[-2])
    return result


def merge(arr1: list, arr2: list) -> list:
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr[:]
    mid = len(arr) // 2
    sub_arr1 = merge_sort(arr[:mid])
    sub_arr2 = merge_sort(arr[mid:])
    result = merge(sub_arr1, sub_arr2)
    return result


def merge_sort2(arr: list) -> list:
    return arr[:] if len(arr) == 1 else merge(merge_sort2(arr[:len(arr) // 2]), merge_sort2(arr[len(arr) // 2:]))


def get_all_passwords(chars: set) -> list:
    if not chars:
        return ['']

    passwords = []
    for char in chars:
        for password in get_all_passwords(chars - {char}):
            passwords.append(char + password)
    return passwords


if __name__ == "__main__":
    print(merge_sort2([2, 5, 4, 1, 8, 0]))
    print(get_all_passwords({'a', 'b', 'c'}))
    print(fib(10))
    print(fib_list(10))
