class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = r = i = 0
        tempnums1 = nums1[::]

        while l < m and r < n:
            if tempnums1[l] <= nums2[r]:
                nums1[i] = tempnums1[l]
                l += 1
            elif tempnums1[l] > nums2[r]:
                nums1[i] = nums2[r]
                r += 1
            i += 1

        while l < m:
            nums1[i] = tempnums1[l]
            l += 1
            i += 1

        while r < n:
            nums1[i] = nums2[r]
            r += 1
            i += 1

        