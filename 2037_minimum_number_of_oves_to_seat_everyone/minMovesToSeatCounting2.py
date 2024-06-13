from ast import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        l = 101

        count = [0] * l

        for i in range(n):
            count[seats[i]] += 1
            count[students[i]] -= 1

        res = 0
        current = 0

        for i in count:
            res += abs(current)
            current += i

        return res