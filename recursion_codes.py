def fib(index: int) -> int:
    if index == 0:
        return 0
    if index == 1:
        return 1
    result = fib(index - 2) + fib(index - 1)
    return result


def fib_list(index: int) -> list:
    if index == 0:
        return [0]
    if index == 1:
        return [0, 1]

    lst = fib_list(index - 1)
    lst.append(lst[-1] + lst[-2])
    return lst


def get_all_passwords(chars: set) -> list:
    if not chars:
        return ['']
    passwords = []
    for char in chars:
        sub_passwords = get_all_passwords(chars - {char})
        for sub_password in sub_passwords:
            passwords.append(char + sub_password)
    return passwords


def merge(arr1: list, arr2: list) -> list:
    i = 0
    j = 0
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
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    sub_arr1 = merge_sort(arr[:mid])
    sub_arr2 = merge_sort(arr[mid:])
    result = merge(sub_arr1, sub_arr2)
    return result


def merge_sort2(arr: list) -> list:
    return arr if len(arr) <= 1 else merge(merge_sort2(arr[:len(arr) // 2]), merge_sort2(arr[len(arr) // 2:]))


merge_sort3 = lambda x: x if len(x) <= 1 else merge(merge_sort3(x[:len(x) // 2]), merge_sort3(x[len(x) // 2:]))

if __name__ == "__main__":
    print(fib(3))
    print(fib_list(10))
    print(get_all_passwords({'a'}))
    print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(merge_sort2([2, 8, 3, 0, 6, 1]))
    print(merge_sort3([6, 3, 4, 9, 1, 0]))
