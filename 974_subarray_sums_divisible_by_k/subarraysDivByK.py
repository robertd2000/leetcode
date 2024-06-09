class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [1] + [0] * k
        s = 0
        res = 0

        for num in nums:
            s = (s + num) % k
            res += count[s]
            count[s] += 1


        return res