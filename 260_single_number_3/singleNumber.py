from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash = {}

        res = []

        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1

        for key, item in hash.items():
            if item == 1:
                res.append(key)
        return res