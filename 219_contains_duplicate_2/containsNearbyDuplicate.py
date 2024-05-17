from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for i, value in enumerate(nums):
            if value in hashMap and abs(hashMap[value] - i) <= k:
                return True
            hashMap[value] = i

        return False