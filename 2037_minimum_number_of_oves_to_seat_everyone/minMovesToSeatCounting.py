from ast import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        l = 101

        countSeats = [0] * l
        countStudents = [0] * l

        for i in range(n):
            countSeats[seats[i]] += 1
            countStudents[students[i]] += 1

        p1 = p2 = 0

        for i in range(l):
            while countSeats[i] > 0:
                seats[p1] = i
                p1 += 1
                countSeats[i] -= 1

            while countStudents[i] > 0:
                students[p2] = i
                p2 += 1
                countStudents[i] -= 1

        res = 0

        for i in range(n):
            moves = abs(students[i] - seats[i])
            res += moves

        return res