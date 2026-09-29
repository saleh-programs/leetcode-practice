class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        current = intervals[0][1]

        for i in range(1, len(intervals)):
            if current <= intervals[i][0]:
                current = intervals[i][1]
                continue
            res += 1
            current = min(current, intervals[i][1])

        return res
