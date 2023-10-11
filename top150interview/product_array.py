from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n
        res = 1

        for i in range(n):
            product[i] = res
            res *= nums[i]

        res = 1

        for i in range(n - 1, -1, -1):
            product[i] *= res
            res *= nums[i]

        return product
