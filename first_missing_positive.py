
def missing_number(nums: list) -> int:
    print("input array = {}".format(nums))
    extra_num = 0

    # Remove unwanted numbers
    i = 0
    while i < len(nums):
        if nums[i] < 0 or nums[i] > len(nums):
            nums[i] = 0
        i += 1

    # Marks the index of available numbers
    i = 0
    while i < len(nums):
        if nums[i] == float('-inf'):
            nums[0] = abs(nums[0]) * -1
        else:
            if abs(nums[i]) == len(nums):
                extra_num = float('-inf')
            else:
                nums[abs(nums[i])] = (abs(nums[abs(nums[i])]) * -1) if nums[abs(nums[i])] != 0 else float('-inf')
        i += 1

    print("Transformed Array = {}".format(nums))

    # Check the unmarked index
    i = 1
    while i < len(nums):
        if nums[i] >= 0:
            return i
        i += 1
    else:
        if extra_num < 0:
            return i+1
        else:
            return i




arr = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]

#arr = [3, 4, -1, 1]
# arr = [1, 2, 0]

print("length_arr = {}".format(len(arr)))
print(missing_number(arr))
