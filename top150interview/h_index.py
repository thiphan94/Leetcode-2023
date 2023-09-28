from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations) == 1 and citations[0] == 0:
            return 0
        else:
            for i, elt in enumerate(citations):
                if elt < i + 1:
                    return i

        return len(citations)
