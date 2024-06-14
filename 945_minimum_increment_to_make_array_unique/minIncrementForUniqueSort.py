from ast import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        count = 0

        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += nums[i] + 1 - nums[i + 1]
                nums[i + 1] = nums[i] + 1

        return count