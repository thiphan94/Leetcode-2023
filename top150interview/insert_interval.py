class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        inserted = False

        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
            else:  # Overlapping intervals
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        if not inserted:
            res.append(newInterval)

        return res
