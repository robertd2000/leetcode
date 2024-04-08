from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        n = len(nums)
        pre = 1
        post = 1

        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
            res[n - i - 1] *= post
            post *= nums[n - i - 1]

        return res