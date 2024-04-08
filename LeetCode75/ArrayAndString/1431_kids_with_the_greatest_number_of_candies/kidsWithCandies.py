from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_max = max(candies)
        res = []

        for i in candies:
            if i + extraCandies >= candies_max:
                res.append(True)
            else:
                res.append(False)

        return res