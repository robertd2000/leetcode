class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2
        res = [[0] * m for i in range(m)]

        for i in range(m):
            for j in range(m):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[k][l])



        return res
        