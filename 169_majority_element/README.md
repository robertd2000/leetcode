# [169. Majority Element](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

Given an array `nums` of size `n`, return the _majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Example 1:

```
Input: nums = [3,2,3]
Output: 3
```

## Example 2:

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints:

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

_Follow-up:_ Could you solve the problem in linear time and in `O(1)` space?

## Code

**Sort**

```python

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        nums.sort()

        return nums[mid]

```

**Hash**

```python

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] = hash[i] + 1
            else:
                hash[i] = 1

        n = len(nums) // 2

        for key, val in hash.items():
            if val > n:
                return key

```
