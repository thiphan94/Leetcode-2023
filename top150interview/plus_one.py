from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(integer) for integer in digits])) + 1
        return [int(x) for x in str(num)]
