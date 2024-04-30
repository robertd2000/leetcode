# [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150)

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i] and`
- `i + j < n`

Return _the minimum number of jumps to reach_ `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

## Example 1:

```

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

## Example 2:

```

Input: nums = [2,3,0,1,4]
Output: 2

```

## Constraints:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

```python

class Solution:
    def jump(self, nums: List[int]) -> int:
        k = j = c = 0

        for i in range(len(nums) - 1):
            j = max(j, nums[i] + i)
            if i == k:
                c += 1
                k = j

        return c

```

```java

class Solution {
    public int jump(int[] nums) {
        int reach = 0;
        int jumped = 0;
        int count = 0;
        int i = 0;

        while (i < nums.length - 1) {
            reach = Math.max(reach, nums[i] + i);

            if (i == jumped) {
                jumped = reach;
                count++;
            }
            i++;
        }

        return count;
    }
}

```
