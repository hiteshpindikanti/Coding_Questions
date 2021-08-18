def get_set_bit_count(num: int):
    bit_set_count = 0
    while num > 0:
        if num % 2:
            bit_set_count += 1
        num //= 2
    return bit_set_count


if __name__ == "__main__":
    print(get_set_bit_count(1023))
