import math


def binary_to_string(num:float, limit:int=32) -> str:
    numerator, denominator = float.as_integer_ratio(num)
    significant_bits = math.log2(denominator)
    if significant_bits > limit:
        return "ERROR"
    else:
        s = bin(numerator)[2:]
        zero_str = '0'*(denominator - len(s))
        return '0b' + zero_str + s


print(binary_to_string(0.75))