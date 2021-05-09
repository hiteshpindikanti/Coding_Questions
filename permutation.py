def calculate(nums: list) -> list:
    if len(nums) == 1:
        return [nums[0]]
    answer = []
    options = calculate(nums[1:])
    answer.extend(list(map(lambda x: str(nums[0]) + "+" + str(x), options)))
    answer.extend(list(map(lambda x: str(nums[0]) + "-" + str(x), options)))
    answer.extend(list(map(lambda x: str(nums[0]) + "*" + str(x), options)))
    answer.extend(list(map(lambda x: str(nums[0]) + "/" + str(x), options)))
    return answer


def permutations(nums: list) -> list:
    ans = []
    if len(nums) == 1:
        return [nums]
    for i in range(len(nums)):
        ans.extend(list(map(lambda x: [nums[i]] + x, permutations(nums[:i] + nums[i + 1:]))))
    return ans


arr = [24, 5, 3, 100, 80, 16]
arrs = permutations(arr)

for ar in arrs:
    option = calculate(ar)
    for e in option:
        ans = eval(e)
        print("{} = {}".format(e, ans))
        if ans == 678:
            print(e)
            break
    else:
        continue
    break
