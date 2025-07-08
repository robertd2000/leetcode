from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        p1 = 0
        p2 = 0

        for num in nums:
            p1, p2 = max(p1, p2 + num), p1

        return p1