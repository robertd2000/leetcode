# [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/)

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner._

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

## Example 1:

![Example 1](image.png)

```

Input: m = 3, n = 7
Output: 28

```

## Example 2:

```

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

## Constraints:

- `1 <= m, n <= 100`

# Code

```py

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for x in range(n + 1)] for y in range(m + 1)]
        print(arr)
        return self.helper(m, n, arr)

    def helper(self, m: int, n: int, arr: List[List[int]]) -> int:
        if n == 1 and m == 1:
            return 1
        if n < 1 or m < 1:
            return 0

        if arr[m][n] != 0:
            return arr[m][n]

        arr[m][n] = self.helper(m - 1, n, arr) + self.helper(m, n - 1, arr)
        return arr[m][n]

```

```java

class Solution {
    public int uniquePaths(int m, int n) {
        return helper(m, n, new int[m + 1][n + 1]);
    }

    public int helper(int m, int n, int[][] arr) {
        if (m == 1 && n == 1) {
            return 1;
        }

        if (m < 1 || n < 1) {
            return 0;
        }

        if (arr[m][n] != 0) {
            return arr[m][n];
        }

        arr[m][n] = helper(m - 1, n, arr) + helper(m, n - 1, arr);
        return arr[m][n];
    }
}

```

```ts
function uniquePaths(m: number, n: number): number {
  return helper(
    m,
    n,
    Array.from(Array(m + 1), () => new Array(n + 1))
  );
}

function helper(m: number, n: number, arr: number[][]): number {
  if (m == 1 && n == 1) return 1;
  if (m < 1 || n < 1) return 0;

  if (arr[m][n]) return arr[m][n];

  arr[m][n] = helper(m - 1, n, arr) + helper(m, n - 1, arr);

  return arr[m][n];
}
```
