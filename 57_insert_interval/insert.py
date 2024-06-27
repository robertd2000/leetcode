class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)

        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]

        res.append(newInterval)

        return res