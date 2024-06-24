class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        startColor = image[sr][sc]

        if startColor == color:
            return image

        def mark(row, col):
            if row < 0 or row >= m:
                return
            if col < 0 or col >= n:
                return
            if image[row][col] != startColor:
                return

            image[row][col] = color

            mark(row, col - 1)
            mark(row, col + 1)
            mark(row - 1, col)
            mark(row + 1, col)

        mark(sr, sc)

        return image