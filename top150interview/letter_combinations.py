from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keymap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = ["".join(x) for x in product(*(keymap[i] for i in digits)) if x]

        return combinations
