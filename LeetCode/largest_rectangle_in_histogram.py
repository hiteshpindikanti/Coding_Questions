def get_largest_rectangle_area(heights: list) -> float:
    if len(heights) == 0:
        return 0
    elif len(heights) == 1:
        return heights[0]
    mid = len(heights) // 2
    area1 = get_largest_rectangle_area(heights[:mid])
    area2 = get_largest_rectangle_area(heights[mid + 1:])
    area3 = get_largest_rectangle_area_including_mid(heights)

    return max(area1, area2, area3)


def get_largest_rectangle_area_including_mid(heights: list) -> float:
    if len(heights) == 2:
        return max(*heights, min(heights) * 2)
    mid = len(heights) // 2
    i = mid - 1
    j = mid + 1
    max_area = heights[mid]
    current_rectangle = {'height': heights[mid], 'start': mid, 'end': mid}
    while True:
        if (i >= 0 and j < len(heights) and heights[i] > heights[j]) or (j == len(heights)):
            current_rectangle = {'height': min(current_rectangle['height'], heights[i]),
                                 'start': i, 'end': current_rectangle['end']}
            max_area = max(max_area,
                           current_rectangle['height'] * (current_rectangle['end'] - current_rectangle['start'] + 1))
            i -= 1
        else:
            current_rectangle = {'height': min(current_rectangle['height'], heights[j]),
                                 'start': current_rectangle['start'], 'end': j}
            max_area = max(max_area,
                           current_rectangle['height'] * (current_rectangle['end'] - current_rectangle['start'] + 1))
            j += 1
        if i < 0 and j == len(heights):
            break

    return max_area


if __name__ == "__main__":
    print(get_largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # ANS = 10
    print(get_largest_rectangle_area([2, 4]))  # ANS = 4
    print(get_largest_rectangle_area([1, 2, 2]))  # ANS = 4
