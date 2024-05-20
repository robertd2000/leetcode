# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150)

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length of a
subarray** whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Example 1:

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

## Example 2:

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

## Example 3:

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints:

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

```python

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        i, j, s, res = 0, 0, 0, n + 1

        while j < n:
            s += nums[j]
            j += 1

            while s >= target:
                res = min(res, j - i)
                s -= nums[i]
                i += 1

        return res if res < n + 1 else 0

```

```java

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int j = 0;
        int i = 0;
        int sum = 0;
        int res = n + 1;

        while (j < n) {
            sum += nums[j];
            j++;

            while (sum >= target) {
                res = Math.min(res, j - i);
                sum -= nums[i];
                i++;
            }
        }

        return res <= n ? res : 0;
    }
}

```
