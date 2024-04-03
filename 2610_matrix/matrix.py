from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        j = 0
        k = 0

        pov = [nums]
        while k < len(nums):
            subarr = []
            p = []

            for i in pov[j]:
                if i not in subarr:
                    subarr.append(i)
                    k += 1
                else:
                    p.append(i)
            j += 1
            pov.append(p)
            res.append(subarr)

        return res
