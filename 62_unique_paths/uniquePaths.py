class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for x in range(n + 1)] for y in range(m + 1)]
        print(arr)
        return self.helper(m, n, arr)

    def helper(self, m: int, n: int, arr: List[List[int]]) -> int:
        if n == 1 and m == 1:
            return 1
        if n < 1 or m < 1:
            return 0

        if arr[m][n] != 0:
            return arr[m][n]

        arr[m][n] = self.helper(m - 1, n, arr) + self.helper(m, n - 1, arr)
        return arr[m][n]