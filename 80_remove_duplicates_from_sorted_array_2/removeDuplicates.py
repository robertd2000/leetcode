class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        for i in range(len(nums)):
            if idx < 2 or nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx += 1
        return idx