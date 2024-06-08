class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {
            0: -1
        }
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            if k != 0:
                s %= k
            if s not in map:
                map[s] = i
            elif i - map[s] > 1:
                return True


        return False