import unittest
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # adding extraCandies to each element
        new_values = [x + extraCandies for x in candies]

        return [number >= max(candies) for number in new_values]

class TestGreatestCandies(unittest.TestCase):
    def test_greatest_candies(self):
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies([2,3,5,1,3], 3), [True,True,True,False,True])
        self.assertEqual(solution.kidsWithCandies([4,2,1,1,2], 1), [True,False,False,False,False])
        self.assertEqual(solution.kidsWithCandies([12,1,12], 10), [True,False,True])

if __name__ == '__main__':
    unittest.main()