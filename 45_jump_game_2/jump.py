class Solution:
    def jump(self, nums: List[int]) -> int:
        k = j = c = 0

        for i in range(len(nums) - 1):
            j = max(j, nums[i] + i)
            if i == k:
                c += 1
                k = j
        
        return c
