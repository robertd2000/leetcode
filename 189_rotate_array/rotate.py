class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n == k:
            return

        if n == 1:
            return
        r = n - (k % n)
        temp = nums[::]

        for l in range(n):
            if r < n:
                nums[l] = temp[r]
                nums[r] = temp[l]
                if k > n and r == n:
                    r = n - k
            else:
                if abs(l - k) <= n:
                    nums[l] = temp[l - k]
            r += 1
