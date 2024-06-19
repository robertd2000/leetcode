from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        left, right = 1, max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for i in bloomDay:
                flow = 0 if i > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m:
                        break
            if bouq == m:
                right = mid
            else:
                left = mid + 1

        return left
            