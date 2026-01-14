# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

## Example 1:

```

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

## Example 2:

```

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

## Example 3:

```

Input: nums = [1,0,1,2]
Output: 3

```

## Constraints:

- `1 <= s.length <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution

```py

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)

        m = 0

        for x in n:
            if x - 1 in n:
                continue
            y = x + 1
            while y in n:
                y = y + 1
            m = max(m, y - x)

        return m

```

```go

func longestConsecutive(nums []int) int {
    set := make(map[int]struct{})

    for _, n := range nums {
        set[n] = struct{}{}
    }

    res := 0

    for x := range set {
        if _, ok := set[x - 1]; ok {
            continue
        }

        y := x + 1

        for {
            if _, ok := set[y]; !ok {
                break
            }

            y += 1
        }

        res = max(res, y - x)
    }

    return res
}

```

```go

function longestConsecutive(nums: number[]): number {
    const numsSet = new Set(nums)
    let res = 0

    for (let x of numsSet) {
        if (numsSet.has(x - 1)) continue

        let y = x + 1

        while (numsSet.has(y)) {
            y++
        }

        res = Math.max(res, y - x)
    }

    return res
};

```
