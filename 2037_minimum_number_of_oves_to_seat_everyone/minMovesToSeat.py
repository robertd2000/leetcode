from ast import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()

        res = 0

        for i in range(n):
            moves = abs(students[i] - seats[i])
            res += moves

        return res