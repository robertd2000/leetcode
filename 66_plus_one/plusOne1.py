from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        k = 0
        res = [0] * n
        digits[-1] = digits[-1] + 1
        for i in range(n - 1, -1, -1):
            s = digits[i]
            a = s if s <= 9 else 0

            if k == 1:
                a += k

            if s >= 10:
                k = 1
            else:
                k = 0
            if a >= 10:
                a = 0
                k = 1
            res[i] = a

        if k == 1:
            res.insert(0, 1)
        return res