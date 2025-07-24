# [326. Power of Three](https://leetcode.com/problems/power-of-three/description/)

Given an integer n, return true if it is a power of three. Otherwise, return `false`.

An integer n is a power of three, if there exists an integer x such that `n == 3x`.

## Example 1:

```
Input: n = 27
Output: true
Explanation: 27 = 3^3
```

## Example 2:

```
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.
```

## Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

## Constraints:

- `-2^31 <= nums[i] <= 2^31 - 1`

```python

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

```
