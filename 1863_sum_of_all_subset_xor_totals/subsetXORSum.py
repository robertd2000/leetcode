from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        b = 0
        for i in nums:
            b |= i

        return b * int(pow(2, len(nums) - 1))