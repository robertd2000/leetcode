class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        if n < 2:
            return 1

        prev = 1
        curr = 1

        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr