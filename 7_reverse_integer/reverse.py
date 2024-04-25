class Solution:
    def reverse(self, x: int) -> int:
        xs = str(x)
        xs = xs[::-1]

        if xs[-1] == '-':
            xs = '-' + xs[:-1]

        res = int(xs)

        if res > pow(2, 31) - 1 or res < -pow(2, 31) - 1:
            return 0
        return res