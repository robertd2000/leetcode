from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        m = n + 1

        s = (n * m) // 2

        return s - sum(nums)
