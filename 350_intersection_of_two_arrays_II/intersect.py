from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        res = []

        h = defaultdict(int)

        for i in nums1:
            h[i] += 1

        for i in nums2:
            if i in h and h[i] > 0:
                res.append(i)
                h[i] -= 1

        return res