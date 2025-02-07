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

  const results: number[][] = [intervals[0]];

  for (let interval of intervals) {
    const recent = results[results.length - 1];
    if (recent[1] >= interval[0]) {
      recent[1] = Math.max(recent[1], interval[1]);
    } else {
      results.push(interval);
    }
  }

  return results;
}
```

```py

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals:
            prev = res[-1]
            if prev[1] >= interval[0]:
                prev[1] = max(interval[1], prev[1])
            else:
                res.append(interval)

        return res

```

```java

class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;
        if (n <= 1)
			return intervals;

		Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        Stack<int[]> res = new Stack<>();
        res.add(intervals[0]);

        for (int[] interval : intervals) {
            int[] prev = res.peek();

            if (prev[1] >= interval[0]) {
                prev[1] = Math.max(prev[1], interval[1]);
            } else {
                res.add(interval);
            }
        }

		return res.toArray(new int[res.size()][]);
    }
}

```

```cpp

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
      vector<vector<int>> res;
      sort(intervals.begin(), intervals.end());

      for (auto interval : intervals) {
          if (res.empty() || res.back()[1] < interval[0]) {
              res.push_back(interval);
          } else {
              res.back()[1] = max(res.back()[1], interval[1]);
          }
      }

      return res;
  }

  static bool comp(vector<int> a, vector<int> b) { return a[0] > b[0]; }
};

```

```go

func merge(intervals [][]int) [][]int {
	var res [][]int

	sort.Slice(intervals, func(i, j int) bool {
		if len(intervals[i]) == 0 && len(intervals[j]) == 0 {
			return false
		}
		if len(intervals[i]) == 0 || len(intervals[j]) == 0 {
			return len(intervals[i]) == 0
		}

		return intervals[i][0] < intervals[j][0]
	})

	res = append(res, intervals[0])

	for _, interval := range intervals {
		n := len(res) - 1
		if res[n][1] >= interval[0] {
			res[n][1] = max(res[n][1], interval[1])
		} else {
			res = append(res, interval)
		}
	}

	return res
}

func max(a int, b int) int {
	if a > b {
		return a
	}

	return b
}

```
