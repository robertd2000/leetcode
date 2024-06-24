class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        res = 0
        mid = nums[n // 2]

        for num in nums:
            res += abs(mid - num)

        return res