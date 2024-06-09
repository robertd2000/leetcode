class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        if matrix == None or n == 0 or m == 0:
            return False

        col = 0
        row = m - 1

        while col < n and row >= 0:
            if matrix[col][row] == target:
                return True
            if matrix[col][row] > target:
                row -= 1
            else:
                col += 1

        return False