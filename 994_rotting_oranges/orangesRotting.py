from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        if grid is None or rowLen == 0:
            return -1
        colLen = len(grid[0])

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 2:
                    self.rott(grid, row, col, 2)

        minutes = 2

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 1:
                    return -1
                minutes = max(minutes, grid[row][col])

        return minutes - 2

    def rott(self, grid: List[List[int]], row: int, col: int, minutes: int):
        rowLen = len(grid)
        colLen = len(grid[0])

        if (
            row < 0
            or row >= rowLen
            or col < 0
            or col >= colLen
            or grid[row][col] == 0
            or grid[row][col] > 1
            and grid[row][col] < minutes
        ):
            return
        else:
            grid[row][col] = minutes
            self.rott(grid, row, col - 1, minutes + 1)
            self.rott(grid, row, col + 1, minutes + 1)
            self.rott(grid, row - 1, col, minutes + 1)
            self.rott(grid, row + 1, col, minutes + 1)