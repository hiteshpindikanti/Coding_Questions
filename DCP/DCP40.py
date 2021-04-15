import time


def find_unique1(arr: list) -> int:
    result = binary(arr[0])
    i = 1
    while i < len(arr):
        result = xor(result, binary(arr[i]))
        i += 1

    return int(''.join(map(str, result)), 2)


def binary(n: int) -> list:
    return [int(i) for i in bin(n)[2:]]


def xor(binary1: list, binary2: list):
    result = []
    length = max(len(binary1), len(binary2))
    binary1 = [0] * (length - len(binary1)) + binary1
    binary2 = [0] * (length - len(binary2)) + binary2

    i = 0
    while i < length:
        result.append((binary1[i] + binary2[i]) % 3)
        i += 1

    return result


def find_unique2(arr):
    result_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            result_arr[i] = (result_arr[i] + bit) % 3

    result = 0
    for i, bit in enumerate(result_arr):
        if bit:
            result += 2 ** i

    return result


a = [3, 10, 3, 3, 10, 10] * 10 ** 5 + [2]
start = time.time()
print(find_unique1(a))
end = time.time()
print('time taken: {} secs'.format(end - start))

start = time.time()
print(find_unique2(a))
end = time.time()
print('time taken: {} secs'.format(end - start))
