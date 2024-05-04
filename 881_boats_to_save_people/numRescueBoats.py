class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c = 0
        n = len(people)
        l, r = 0, n - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            c += 1

        return c


        return c