from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        next = 0
        current = 0
        for i in range(0, len(nums) - 1):
            next = max(next, i + nums[i])
            if current == i:
                step += 1
                current = next

        return step
