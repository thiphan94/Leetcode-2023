from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_set = set()
        for i in range(len(trust)):
            if trust[i][0] not in trust_set:
                trust_set.add(trust[i][0])

        res = 0
        for i in range(1, n + 1):
            if i not in trust_set:
                res = i
        for i in range(1, n + 1):
            if [i, res] not in trust and i != res:
                return -1
        return res
