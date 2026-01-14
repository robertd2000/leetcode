# [120. Triangle](https://leetcode.com/problems/triangle/description/)

Given a triangle array, return the minimum path `sum` from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index `i` or index `i + 1` on the next row.

## Example 1:

```

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

```

## Example 2:

```

Input: triangle = [[-10]]
Output: -10

```

## Constraints:

- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

The idea is to go bottom-up from the bottom of the triangle. We do this by looking starting at the 2nd to last row of the triangle and for each cell, finding the min step of the next row. Then we store that min step + cell value at the current row location. Once we're done with the row, we move up, so by the time we're at the top of the triangle, we have the minimal sum stored in the [0][0] location.

## Solution

```ts
function minimumTotal(triangle: number[][]): number {
  for (let r = triangle.length - 2; r >= 0; r--) {
    for (let l = 0; l <= r; l++) {
      triangle[r][l] += Math.min(triangle[r + 1][l], triangle[r + 1][l + 1]);
    }
  }

  return triangle[0][0];
}
```
