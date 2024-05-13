class Solution:
        def matrixScore(self, A):
            n, m = len(A), len(A[0])
            res = (1 << m - 1) * n
            for j in range(1, m):
                cur = sum(A[i][j] == A[i][0] for i in range(n))
                res += max(cur, n - cur) * (1 << m - 1 - j)
            return res
        