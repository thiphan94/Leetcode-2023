from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_amount = 0

        while left < right:
            amount = min(height[left], height[right]) * (right - left)
            max_amount = max(max_amount, amount)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount
