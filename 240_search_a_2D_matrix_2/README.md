# [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

## Example 1:

![Example 1](image-1.png)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

## Example 2:

![Example 2](image.png)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

## Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n`, `m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`

**Follow-up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Code

**Hash table**

```python

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        if matrix == None or n == 0 or m == 0:
            return False

        col = 0
        row = m - 1

        while col < n and row >= 0:
            if matrix[col][row] == target:
                return True
            if matrix[col][row] > target:
                row -= 1
            else:
                col += 1

        return False

```

```java

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        if (matrix == null || m == 0 || n == 0) {
            return false;
        }

        int c = 0;
        int r = n - 1;

        while (c < m && r >= 0) {
            if (matrix[c][r] == target) {
                return true;
            }

            if (matrix[c][r] > target) {
                r--;
            } else {
                c++;
            }
        }

        return false;
    }
}

```

```ts
function searchMatrix(matrix: number[][], target: number): boolean {
  const n = matrix.length;
  const m = matrix[0].length;

  let row = 0;
  let col = m - 1;

  while (row < n && col >= 0) {
    if (matrix[row][col] === target) {
      return true;
    } else if (matrix[row][col] > target) {
      col--;
    } else {
      row++;
    }
  }

  return false;
}
```
