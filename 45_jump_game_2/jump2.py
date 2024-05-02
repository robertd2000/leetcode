class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = count = 0
        n = len(nums) - 1
        while right < n:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(nums[i] + i, farthest)

            left = right + 1
            right = farthest
            count += 1

        return count
        