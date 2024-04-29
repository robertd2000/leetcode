class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        for i in range(len(nums)):
            if j < i: 
                return False
            j = max([i + nums[i], j])

        return True