# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

## Example 1:

```
Input: nums = [1,3,4,2,2]
Output: 2
```

## Example 2:

```
Input: nums = [3,1,3,4,2]
Output: 3
```

## Example 2:

```
Input: nums = [3,3,3,3,3]
Output: 3
```

## Constraints:

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in nums appear only once except for precisely one integer which appears two or more times.

## Code

```py

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1

        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow


```

```go

func findDuplicate(nums []int) int {
	n := len(nums)

	if n < 1 {
		return -1
	}

	slow, fast := nums[0], nums[nums[0]]

	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}

	fast = 0

	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}

	return slow
}

```

```ts
function findDuplicate(nums: number[]): number {
  let n = nums.length;

  if (n < 1) return -1;

  let slow = nums[0];
  let fast = nums[nums[0]];

  while (slow != fast) {
    slow = nums[slow];
    fast = nums[nums[fast]];
  }

  fast = 0;

  while (slow != fast) {
    slow = nums[slow];
    fast = nums[fast];
  }

  return slow;
}
```
