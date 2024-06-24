# [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

**Example 1:**

**Input:** nums = [1,2,3]
**Output:** 2
**Explanation:**
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3] => [2,2,3] => [2,2,2]

**Example 2:**

**Input:** nums = [1,10,2,9]
**Output:** 16

**Constraints:**

- `n == nums.length`
- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

# Code

```python

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        res = 0
        mid = nums[n // 2]

        for num in nums:
            res += abs(mid - num)

        return res

```

```ts
function minMoves2(nums: number[]): number {
  nums.sort((a, b) => a - b);

  const n = nums.length;
  const midIdx = Math.floor(n / 2);
  const mid = nums[midIdx];

  let res = 0;

  for (let num of nums) {
    res += Math.abs(mid - num);
  }

  return res;
}
```
