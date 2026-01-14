class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)

        m = 0

        for x in n:
            if x - 1 in n:
                continue
            y = x + 1
            while y in n:
                y = y + 1
            m = max(m, y - x)

        return m