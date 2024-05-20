from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.back(nums, 0, 0)
        
    def back(self, nums: List[int], index: int, current: int) -> int:
        if index == len(nums):
            return current
        
        withElement = self.back(nums, index + 1, current ^ nums[index])
        withoutElement = self.back(nums, index + 1, current)

        return withElement + withoutElement