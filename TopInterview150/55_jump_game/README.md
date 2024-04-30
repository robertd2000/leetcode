# [55. Jump Game](https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150)

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index, or `false` otherwise_.

## Example 1:

```

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

## Example 2:

```

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

## Constraints:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

```python

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        for i in range(len(nums)):
            if j < i:
                return False
            j = max([i + nums[i], j])

        return True

```

```java

class Solution {
    public boolean canJump(int[] nums) {
        int reach = 0;
        int n = nums.length;
        int i;

        for (i = 0; i < n && i <= reach; i++) {
            reach = Math.max(reach, i + nums[i]);
        }

        return i == n;
    }
}

```
