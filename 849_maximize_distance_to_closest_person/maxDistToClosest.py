from math import ceil
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = 0
        n = len(seats)

        count = 0
        start = 0

        for i in range(n):
            if seats[i] == 0:
                count += 1
                if i == n - 1 or start == 0:
                    maxDistance = max(maxDistance, count)
                else:
                    maxDistance = max(maxDistance, ceil(count / 2))
            else:
                count = 0
                start = i + 1
        
        return maxDistance