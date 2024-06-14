# [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14)

You are given an integer array `nums`. In one move, you can pick an index `i` where `0 <= i < nums.length` and increment `nums[i]` by `1`.

Return *the minimum number of moves to make every value in* `nums` **_unique_**.

The test cases are generated so that the answer fits in a 32-bit integer.

**Example 1:**

**Input:** nums = [1,2,2]
**Output:** 1
**Explanation:** After 1 move, the array could be [1, 2, 3].

**Example 2:**

**Input:** nums = [3,2,1,2,1,7]
**Output:** 6
**Explanation:** After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

**Constraints:**

- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 105`

## Code

**Sort**

```python

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        count = 0

        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += nums[i] + 1 - nums[i + 1]
                nums[i + 1] = nums[i] + 1

        return count

```

```ts
function minIncrementForUnique(nums: number[]): number {
  nums.sort((a, b) => a - b);

  let count = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] >= nums[i + 1]) {
      count += nums[i] + 1 - nums[i + 1];
      nums[i + 1] = nums[i] + 1;
    }
  }

  return count;
}
```

**Map**

```py
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        root = {}

        def find(x):
            value = find(root[x] + 1) if x in root else x
            root[x] = value

            return root[x]

        return sum(find(num) - num for num in nums)

```

```ts
function minIncrementForUnique(nums: number[]): number {
  const root = new Map();

  function find(x: number): number {
    const value = root.has(x) ? find(root.get(x) + 1) : x;
    root.set(x, value);
    return root.get(x);
  }

  return nums.reduce((a, v) => (a += find(v) - v), 0);
}
```
