from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0

        pos = k

        while True:
            if tickets[pos] == 0:
                return count

            if tickets[0] == 0:
                val = tickets.pop(0)
                tickets.append(val)
                if pos == 0:
                    pos = len(tickets) - 1
                else:
                    pos -= 1
            if tickets[0] > 0:
                val = tickets.pop(0)
                tickets.append(val - 1)
                if pos == 0:
                    pos = len(tickets) - 1
                else:
                    pos -= 1

                count += 1

        return count