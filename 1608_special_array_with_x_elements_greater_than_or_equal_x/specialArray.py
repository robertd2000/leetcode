from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        i = 0

        while i < n and nums[i] > i:
            i += 1

        if i < n and i == nums[i]:
            return -1
        return i