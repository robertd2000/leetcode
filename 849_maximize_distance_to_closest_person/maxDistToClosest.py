from math import ceil
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        m = 0
        n = len(seats)

        curr = 0
        start = 0

        for i in range(n):
            if seats[i] == 0:
                curr += 1
                if i == n - 1 or start == 0:
                    m = max(m, curr)
                else:
                    m = max(m, ceil(curr / 2))
            else:
                curr = 0
                start = i + 1


        return m