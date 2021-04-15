def maximum(arr, start, end) -> int:
    max_val = 0
    index = start
    if start < end:
        while start < end:
            if arr[start] > max_val:
                index = start
                max_val = arr[start]
            start += 1
    elif end < start:
        while start > end:
            if arr[start] > max_val:
                index = start
                max_val = arr[start]
            start -= 1
    return index


def addition(arr, start, end, h) -> int:
    s = 0
    while start < end:
        s += arr[start] if arr[start] < h else h
        start += 1
    return s


total_water = 0
height = [5, 4, 1, 2]
i = maximum(height, 0, len(height))
j = i
while i > 0:
    # left_index = height[:i].index(max(height[:i]))
    left_index = maximum(height, 0, i)
    # water = height[left_index] * (i - left_index - 1) - sum(height[left_index + 1:i])
    water = height[left_index] * (i - left_index - 1) - addition(height, left_index + 1, i, height[left_index])
    total_water += water
    print("LEFT: i = {}, left_index = {}, water = {}".format(i, left_index, water))
    i = left_index

while j < len(height) - 1:
    # right_index = j + 1 + (len(height) - j) - 2 - height[j + 1::][::-1].index(max(height[j + 1:]))
    right_index = maximum(height, len(height) - 1, j + 1)
    # water = height[right_index] * (right_index - j - 1) - sum(height[j + 1:right_index])
    water = height[right_index] * (right_index - j - 1) - addition(height, j + 1, right_index, height[right_index])
    total_water += water
    print("RIGHT: j = {}, right_index = {}, water = {}".format(j, right_index, water))
    j = right_index

print("total_water = {}".format(total_water))

# height = [0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 7, 5, 3, 1, 0, 0]
