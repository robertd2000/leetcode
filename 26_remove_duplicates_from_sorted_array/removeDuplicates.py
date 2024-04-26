class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        
        return idx + 1