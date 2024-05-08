from typing import List


Ranks = {
    "1": "Gold Medal",
    "2": "Silver Medal",
    "3": "Bronze Medal",
}


class Solution:
    def getRank(self, val: int) -> str:

        if val > 3:
            return str(val)
        else:
            return Ranks[str(val)]

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        pairs = [[0] * 2 for i in range(n)]

        for i in range(n):
            pairs[i][0] = score[i]
            pairs[i][1] = i

        pairs.sort(key=lambda x: x[0], reverse=True)

        res = [0] * n
        for i in range(n):
            res[pairs[i][1]] = self.getRank(i + 1)

        return res
