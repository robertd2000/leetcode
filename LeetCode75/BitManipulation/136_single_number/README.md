# [136. Single Number](https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75)

Given a **non-empty** array of integers `nums`, every element appears _twice_ except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Example 1:

```
Input: nums = [2,2,1]
Output: 1
```

## Example 2:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

## Example 3:

```
Input: nums = [1]
Output: 1

```

## Constraints:

- `1 <= nums.length <= 3 * 104`
- `-3 * 104 <= nums[i] <= 3 * 104`
- Each element in the array appears twice except for one element which appears only once.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        for key, value in hash.items():
            if value == 1:
                return key

```
