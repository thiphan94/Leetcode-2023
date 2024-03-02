from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        first = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1

            if k < 0:
                k += 1 - nums[first]
                first += 1
            # print(first,i,k,max_len)
            max_len = max(max_len, i - first + 1)
        return max_len
