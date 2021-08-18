from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        for index, num in enumerate(nums):
            self.memo[(index, index)] = num

        return self.max_product(0, len(nums)-1)

    def max_product(self, i: int, j: int) -> int:
        print(f"i={i}, j={j}")
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        mid = (i + j) // 2
        if (i, mid) not in self.memo:
            self.memo[(i, mid)] = self.max_product(i, mid)

        if (mid + 1, j) not in self.memo:
            self.memo[(mid + 1, j)] = self.max_product(mid + 1, j)

        self.memo[(i, j)] = max(self.memo[(i, mid)], self.memo[(mid + 1, j)], self.span(i, j))
        print(f"memo[{i}, {j}] = {self.memo[(i, j)]} | memo[{i}, {mid}] = {self.memo[(i, mid)]} | memo[{mid+1}, {j}] = {self.memo[(mid+1, j)]}")
        return self.memo[(i, j)]

    def span(self, i, j) -> int:
        if i == j:
            return self.nums[i]
        if j == i + 1:
            return self.nums[i] * self.nums[j]

        mid = (i + j) // 2
        left_product = left_product_max = left_product_min = self.nums[mid]
        for index in range(mid-1, i - 1, -1):
            left_product *= self.nums[index]
            left_product_max = max(left_product_max, left_product)
            left_product_min = min(left_product_min, left_product)

        right_product = right_product_max = right_product_min = self.nums[mid + 1]
        for index in range(mid + 2, j + 1):
            right_product *= self.nums[index]
            right_product_max = max(right_product_max, right_product)
            right_product_min = min(right_product_min, right_product)
        result = max(left_product_max * right_product_max, left_product_min * right_product_min)
        print(f"span({i}, {j})= {result} | {left_product_max}, {right_product_max}, {left_product_min}, {right_product_min}")
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([-1,-2,-9,-6]))
