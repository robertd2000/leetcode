class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0

        for _ in range(n):
            k = a + b + c
            a = b
            b = c
            c = k

        return c