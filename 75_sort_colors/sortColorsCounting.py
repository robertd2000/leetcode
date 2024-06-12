class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 4

        for i in nums:
            count[i] += 1

        pos = 0

        for i in range(len(count)):
            for j in range(count[i]):
                nums[pos] = i
                pos += 1

        return nums