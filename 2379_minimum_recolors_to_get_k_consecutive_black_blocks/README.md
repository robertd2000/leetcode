[2379. Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08)
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

**Example 1:**

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
**Example 2:**

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

**Constraints:**

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n

```ts
function minimumRecolors(blocks: string, k: number): number {
  const n = blocks.length;
  let m = n;

  for (let i = 0; i < n - k + 1; i++) {
    let curr_m = 0;
    for (let j = i; j < k + i; j++) {
      if (blocks[j] === "W") curr_m++;
    }
    m = Math.min(m, curr_m);
  }

  return m;
}
```

```ts
function minimumRecolors(blocks: string, k: number): number {
  const n = blocks.length;

  let black = 0;
  let res = n;

  for (let i = 0; i < n; i++) {
    if (i - k >= 0 && blocks[i - k] === "B") {
      black--;
    }

    if (blocks[i] === "B") {
      black++;
    }

    res = Math.min(res, k - black);
  }

  return res;
}
```

```py

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count = 0
        n = len(blocks)
        min_changes = n

        for i in range(n):
            if i - k >= 0 and blocks[i - k] == 'B':
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1
            min_changes = min(min_changes, k - black_count)

        return min_changes

```

```java

class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();

        int black = 0;
        int res = n;

        for (int i = 0; i < n; i++) {
            if (i - k >= 0 && blocks.charAt(i - k) == 'B') black--;
            if (blocks.charAt(i) == 'B') black++;
            res = Math.min(res, k - black);
        }

        return res;
    }
}

```

```cpp

class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int n = blocks.length();

        int min_changes = n;
        int black_count = 0;

        for (int i = 0; i < n; i++) {
            if (i - k >= 0 && blocks[i - k] == 'B') black_count--;
            if (blocks[i] == 'B') black_count++;
            min_changes = min(min_changes, k - black_count);
        }

        return min_changes;
    }
};

```

```go

func minimumRecolors(blocks string, k int) int {
	n := len(blocks)
	black_count := 0
	min_changes := n

    for i := 0; i < n; i++ {
        if i - k >= 0 && blocks[i - k] == 'B' {
            black_count--
        }
        if blocks[i] == 'B' {
            black_count++
        }

        if k - black_count < min_changes {
           min_changes = k - black_count
        }
    }

    return min_changes
}

```
