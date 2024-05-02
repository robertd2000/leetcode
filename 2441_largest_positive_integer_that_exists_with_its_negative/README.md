# [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/?envType=daily-question&envId=2024-05-02)

Given an integer array `nums` that **does not contain** any zeros, find **the largest positive** integer `k` such that `-k` also exists in the array.

Return _the positive integer_ `k`. If there is no such integer, return `-1`.

## Example 1:

```

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

```

## Example 2:

```

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

```

## Example 3:

```

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

```

## Constraints:

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(1)`

# Code

```python

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < 0 and abs(nums[l]) == nums[r]:
                return nums[r]
            if abs(nums[l]) > nums[r]:
                l += 1
            else:
                r -= 1

        return -1

```
