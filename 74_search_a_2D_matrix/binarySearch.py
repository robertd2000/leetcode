class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            isInRow = self.binarySearch(row, target)
            if isInRow:
                return True
        return False

    def binarySearch(self, row: List[int], target: int) -> bool:
        n = len(row)

        l, r = 0, n - 1

        while l <= r:
            mid = int(l + (r - l) / 2)

            if row[mid] == target:
                return True
            if row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
