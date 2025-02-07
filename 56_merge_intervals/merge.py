class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals:
            prev = res[-1]
            if prev[1] >= interval[0]:
                prev[1] = max(interval[1], prev[1])
            else:
                res.append(interval)

        return res