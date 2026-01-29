class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        c = 0

        while r < len(nums):
            c += 1 - nums[r]

            if c > 1:
                c -= 1 - nums[l]
                l += 1

            r += 1

        return r - l - 1
