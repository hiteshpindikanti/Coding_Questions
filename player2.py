def get_valid_interpretation_count(num: str) -> int:
    if not num:
        return 1
    count = 0
    if int(num[0]) > 2:
        count += 1 * get_valid_interpretation_count(num[1:])
    elif int(num[0]) == 2:
        count += 1 * get_valid_interpretation_count(num[1:])
        if len(num) > 1 and 0 <= int(num[1]) <= 5:
            count += 1 * get_valid_interpretation_count(num[2:])
    elif int(num[0]) == 1:
        count += 1 * get_valid_interpretation_count(num[1:])
        if len(num) > 1:
            count += 1 * get_valid_interpretation_count(num[2:])
    else:
        count += 1 * get_valid_interpretation_count(num[1:])
    return count


if __name__ == "__main__":
    print(get_valid_interpretation_count("100200300"))
