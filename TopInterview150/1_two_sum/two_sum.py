class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(0, len(nums)):
            num = target - nums[i]

            if num in hash and hash[num] != i:
                return [i, hash[num]]
            hash[nums[i]] = i