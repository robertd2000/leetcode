from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        frequency = {}

        for i in nums:
            if frequency.get(i, 0) >= len(res):
                res.append([])
            res[frequency.get(i, 0)].append(i)
            frequency[i] = frequency.get(i, 0) + 1

        return res
