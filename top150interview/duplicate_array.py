from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for elt in nums:
            if count < 2 or elt != nums[count - 2]:
                nums[count] = elt
                count += 1
        return count
