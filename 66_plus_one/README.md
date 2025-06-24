[66. Plus One](https://leetcode.com/problems/plus-one/description/)

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

**Example 2:**

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

**Example 3:**

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

**Constraints:**

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s.

```py

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        k = 0
        res = [0] * n
        digits[-1] = digits[-1] + 1
        for i in range(n - 1, -1, -1):
            s = digits[i]
            a = s if s <= 9 else 0

            if k == 1:
                a += k

            if s >= 10:
                k = 1
            else:
                k = 0
            if a >= 10:
                a = 0
                k = 1
            res[i] = a

        if k == 1:
            res.insert(0, 1)
        return res

```

If we add `1` to the last index, the number at the last index will be `0` then we have `carry`. Again if we add the `carry` to the index `0`, the number at index `0` will be `0`, then we will get another `carry`.

Finally, add 1 and 1 will be the first index and return the array.

`return [1,0,0]`

When we add `1` then the number is not `10`, just add `1` to the last index and return the array.

If 10, add 0 to the current index, add `0` to the current index then continue to loop until we find a number except `10` or reach index `0`.

If we reach index `0`, then add `1` to the first index and other all numbers should be `0`, because we have `10` in each digit and have carry for the next digit.

```py

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            digits[i] = 0

            if i == 0:
                return [1] + digits

```
