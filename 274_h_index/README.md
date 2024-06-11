# [274. H-Index](https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150)

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `ith` paper, return _the researcher's h-index._

According to the **definition of h-index on Wikipedia**: The h-index is defined as the maximum value of `h` such that the given researcher has published at least h papers that have each been cited at least `h` times.

## Example 1:

```

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
```

## Example 2:

```

Input: citations = [1,3,1]
Output: 1

```

## Constraints:

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

**Approach 1 (no extra space):**

```python

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        mx = 0
        for i in range(n):
            m = n - citations.index(citations[i], i)
            mx = max(min(m, citations[i]), mx)

        return mx

```

**Approach 2 (counting sort):**

```python

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        buckets = [0] * (n + 1)

        for i in citations:
            if i >= n:
                buckets[n] += 1
            else:
                buckets[i] += 1


        count = 0

        for i in range(n, 0, -1):
            count += buckets[i]
            if count >= i:
                return i

        return 0

```

```ts
function hIndex(citations: number[]): number {
  const n = citations.length;
  const count = new Array<number>(n + 1).fill(0);

  for (let i of citations) {
    if (i > n) {
      count[n]++;
    } else {
      count[i]++;
    }
  }

  let pos = 0;

  for (let i = 0; i <= n; i++) {
    for (let j = 0; j < count[i]; j++) {
      citations[pos] = i;
      pos++;
    }
  }

  let hIndex = 1;

  for (let i = n - 1; i >= 0; i--) {
    if (hIndex > citations[i]) {
      return hIndex - 1;
    }

    hIndex++;
  }

  return n;
}
```
