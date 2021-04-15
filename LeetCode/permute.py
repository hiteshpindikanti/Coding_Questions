
def permute(nums: list) -> list:
    result = []
    if len(nums) == 0:
        return [[]]
    elif len(nums) == 1:
        return [nums]
    else:
        p = permute(nums[1:])
        for row in p:
            for i in range(len(row)+1):
                result.append(row[:i]+[nums[0]]+row[i:])
    return result


array = [1, 3, 2, 4, 5]
permutations = permute(array)
print("length = {}, permulations = {}".format(len(permutations), permutations))


