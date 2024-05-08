# [506. Relative Ranks](https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08)

You are given an integer array `score` of size `n`, where `score[i]` is the score of the `ith` athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are placed based on their scores, where the `1st` place athlete has the highest score, the `2nd` place athlete has the `2nd` highest score, and so on. The placement of each athlete determines their rank:

- The `1st` place athlete's rank is `"Gold Medal"`.
- The `2nd` place athlete's rank is `"Silver Medal"`.
- The `3rd` place athlete's rank is `"Bronze Medal"`.
- For the `4th` place to the `nth` place athlete, their rank is their placement number (i.e., the `xth` place athlete's rank is `"x"`).

Return an array `answer` of size `n` where `answer[i]` is the **rank** of the `ith` athlete.

## Example 1:

```
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
```

## Example 2:

```
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
```

## Constraints:

- `n == score.length`
- `1 <= n <= 10^4`
- `0 <= score[i] <= 10^6`
- All the values in `score` are **unique**.

# Complexity

- **Time complexity:**
  `O(n^2)`

# Code

**Sort**

```python

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

```
