from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            if value == 1:
                return key