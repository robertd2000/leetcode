class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1 = []
        d2 = []
        h1 = {}
        h2 = {}

        for i in nums1:
            h1[i] = i
        for i in nums2:
            h2[i] = i

        for i in nums1:
            if i not in h2 and i not in d1:
                d1.append(i)
        for i in nums2:
            if i not in h1 and i not in d2:
                d2.append(i)
        return [d1, d2]