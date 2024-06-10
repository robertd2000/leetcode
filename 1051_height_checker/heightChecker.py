from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        s = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != s[i]:
                count += 1

        return count