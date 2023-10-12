from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals

        res = []

        intervals.sort(key=lambda x: x[0])

        previous = intervals[0]
        for elt in intervals[1:]:
            if elt[0] <= previous[1]:
                previous[1] = max(previous[1], elt[1])
            else:
                res.append(previous)
                previous = elt
        res.append(previous)
        return res
