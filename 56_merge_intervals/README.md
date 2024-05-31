# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/submissions/1273292019/)

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input._

## Example 1:

```

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

## Example 2:

```

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

## Constraints:

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

```ts
function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]);

  const results = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    if (results.at(-1)[1] >= intervals[i][0]) {
      const prev = results.pop();

      results.push([prev[0], Math.max(prev[1], intervals[i][1])]);
    } else {
      results.push(intervals[i]);
    }
  }

  return results;
}
```
