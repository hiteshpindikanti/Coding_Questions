"""
This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def bins_8(num) -> str:
    bits = 8
    return bin(num & 2 ** (bits + 1) - 1)


def swap_bits(num: int) -> int:
    print(f"{bins_8(num)} = {num}")
    t1 = (num & 170)
    t2 = (num & 85)
    print(f"MASK with 170: {bins_8(t1)}")
    print(f"MASK with 85: {bins_8(t2)}")
    print(f"Right Shift t1: {bins_8(t1 >> 1)}")
    print(f"Left Shift t2: {bins_8(t2 << 1)}")
    print(f"FINAL: {bins_8((t1 >> 1) | (t2 << 1))}")
    return (t1 >> 1) | (t2 << 1)


def swap_bits2(num: int) -> int:
    return (num & 170) >> 1 | (num & 85) << 1


if __name__ == "__main__":
    print(swap_bits(int('11100010', 2)))
    print(swap_bits2(int('11100010', 2)))