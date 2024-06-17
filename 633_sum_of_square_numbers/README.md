# [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-06-17)

Given a non-negative integer `c`, decide whether there're two integers `a` and `b` such that `a2 + b2 = c`.

**Example 1:**

**Input:** c = 5
**Output:** true
**Explanation:** 1 _ 1 + 2 _ 2 = 5

**Example 2:**

**Input:** c = 3
**Output:** false

**Constraints:**

- `0 <= c <= 231 - 1`

# Code

```python

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

```
