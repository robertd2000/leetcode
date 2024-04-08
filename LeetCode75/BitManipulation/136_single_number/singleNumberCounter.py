from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        for i, v in dictionary.items():
            if v == 1:
                return i