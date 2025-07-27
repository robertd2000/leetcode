[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![alt text](PascalTriangleAnimated2.gif)

**Example 1:**

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

**Example 2:**

Input: numRows = 1
Output: [[1]]

**Constraints:**

- `1 <= numRows <= 30`

**Code:**

```py

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [None] * numRows
        for i in range(numRows):
            row, mid = [1] * (i + 1), (i >> 1) + 1
            for j in range(1, mid):
                val = ans[i-1][j-1] + ans[i-1][j]
                row[j], row[len(row)-j-1] = val, val
            ans[i] = row
        return ans


```
