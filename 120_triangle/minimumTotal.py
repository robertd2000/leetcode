from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)]
        dp[n - 1] = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                l = triangle[i][j] + dp[i + 1][j]
                r = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(l, r)

        return dp[0][0]
