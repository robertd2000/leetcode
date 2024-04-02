from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0

        n = len(nums1)
        m = len(nums2)

        res = []

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < n:
            res.append(nums1[i])
            i += 1

        while j < m:
            res.append(nums2[j])
            j += 1

        q = int(len(res) / 2)
        
        if len(res) % 2 == 0:
            return (res[q] + res[q - 1]) / 2
        return res[q]