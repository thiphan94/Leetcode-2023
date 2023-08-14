import unittest
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                n -= 1
                # a flower is planted
                flowerbed[i] = 1
        return n <= 0

class TestGreatestCandies(unittest.TestCase):
    def test_place_flowers(self):
        solution = Solution()
        self.assertEqual(solution.canPlaceFlowers([1,0,0,0,1], 1), True)
        self.assertEqual(solution.canPlaceFlowers([1,0,0,0,1], 2), False)
        self.assertEqual(solution.canPlaceFlowers([1,0,0,0,0,1], 2), False)
        self.assertEqual(solution.canPlaceFlowers([0,0,1,0,0], 1), True)


if __name__ == '__main__':
    unittest.main()