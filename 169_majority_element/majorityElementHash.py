class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] = hash[i] + 1
            else:
                hash[i] = 1

        n = len(nums) // 2

        for key, val in hash.items():
            if val > n:
                return key 