class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        k = 0

        while l <= r:
            if nums[r] == val:
                nums[r] = None
                r -= 1
                k += 1
            elif nums[l] == val:
                nums[l] = nums[r]
                nums[r] = None
                r -= 1
                l += 1
                k += 1

            else:
                l += 1

        return len(nums) - k
