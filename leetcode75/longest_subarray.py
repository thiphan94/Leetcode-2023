from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros_count = 0, 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_count += 1
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            max_len = max(max_len, i - left)
        return max_len
