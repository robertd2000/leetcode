# [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/)

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

**Example 1:**

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

**Example 2:**

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

**Example 3:**

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

**Constraints:**

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

# Code

```py

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        c = 0

        while r < len(nums):
            c += 1 - nums[r]

            if c > 1:
                c -= 1 - nums[l]
                l += 1

            r += 1

        return r - l - 1


```

```go

func longestSubarray(nums []int) int {
	l, r := 0, 0
	c := 0

	for r < len(nums) {
		c += 1 - nums[r]
		if c > 1 {
			c -= 1 - nums[l]
			l++
		}

		r++
	}

	return r - l - 1
}

```
