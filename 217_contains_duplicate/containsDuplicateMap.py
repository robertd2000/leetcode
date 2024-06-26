from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)

        for i in nums:
            map[i] += 1
            if map[i] > 1:
                return True

        return False