from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        triplets = set()
        for i in range(len(nums) - 2):
            first = sorted_list[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                second = sorted_list[j]
                third = sorted_list[k]
                sum_triplet = first + second + third
                if sum_triplet > 0:
                    k -= 1
                if sum_triplet < 0:
                    j += 1
                if sum_triplet == 0:
                    triplets.add((first, second, third))
                    j += 1
                    k -= 1
        return triplets
