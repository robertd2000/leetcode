class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(sqrt(c))
        
        while start <= end:
            powSum = pow(start, 2) + pow(end, 2)

            if powSum == c:
                return True
            elif powSum > c:
                end -= 1
            else:
                start += 1

        return False