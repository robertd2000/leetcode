class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0

        m = len(flowerbed)
        start = 0 if flowerbed[0] == 0 else 1
        end = m if flowerbed[-1] == 0 else m - 1

        for i in range(start, end):
            if (
                (i == 0 or flowerbed[i - 1] == 0)
                and flowerbed[i] == 0
                and (i == m - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                k += 1
        return k >= n
