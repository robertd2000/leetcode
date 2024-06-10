# [1051. Height Checker](https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10)

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the current order that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (0-indexed).

Return _the **number of indices** where `heights[i] != expected[i]`_.

## Example 1:

```
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
```

## Example 2:

```
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
```

## Example 3:

```
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
```

## Constraints:

- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`

# Code

```py

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        s = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != s[i]:
                count += 1

        return count

```

```py

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency = [0] * 101

        for height in heights:
            frequency[height] += 1

        result = 0
        current = 0

        for i in range(len(heights)):
            while frequency[current] == 0:
                current += 1

            if current != heights[i]:
                result += 1
            frequency[current] -= 1

        return result

```

```java

class Solution {
    public int heightChecker(int[] heights) {
        int[] frequency = new int[101];

        for (int height : heights) {
            frequency[height]++;
        }

        int result = 0;
        int currentHeight = 0;

        for (int i = 0; i < heights.length; i++) {
            while (frequency[currentHeight] == 0) {
                currentHeight++;
            }

            if (heights[i] != currentHeight) {
                result++;
            }

            frequency[currentHeight]--;
        }

        return result;
    }
}

```
