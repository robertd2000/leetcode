from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            idx = self.get_index(nums)
            nums[idx] *= multiplier
        return nums


    def get_index(self, nums: List[int]) -> int:
        idx = 0
        res = nums[idx]

        for i in range(len(nums)):
            if nums[i] < res:
                res = nums[i]
                idx = i

        return idx