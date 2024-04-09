from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        for idx, ticket in enumerate(tickets):
            if idx <= k:
                total += min(tickets[idx], tickets[k])
            else:
                total += min(tickets[idx], tickets[k] - 1)

        return total