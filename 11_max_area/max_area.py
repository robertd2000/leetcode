from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height) - 1

        while l < r:
            lH, rH = height[l], height[r]

            square = min(lH, rH) * (r - l)

            if square > maximum:
                maximum = square
            if lH < rH:
                l+= 1  
            else:
                r -= 1

        return maximum