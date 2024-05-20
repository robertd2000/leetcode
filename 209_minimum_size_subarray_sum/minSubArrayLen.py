from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        i, j, s, res = 0, 0, 0, n + 1

        while j < n:
            s += nums[j]
            j += 1

            while s >= target:
                res = min(res, j - i)
                s -= nums[i]
                i += 1

        return res if res < n + 1 else 0
