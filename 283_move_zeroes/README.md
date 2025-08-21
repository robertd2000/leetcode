# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

## Example 1:

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

## Example 2:

```
Input: nums = [0]
Output: [0]
```

## Constraints:

- `1 <= nums.length <= 104`
- `-231 <= nums[i] <= 231 - 1`

```python

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1

```

```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let l = 0;

  for (let r = 0; r < nums.length; r++) {
    if (nums[l] === 0) {
      let temp = nums[l];
      nums[l] = nums[r];
      nums[r] = temp;
    }

    if (nums[l] != 0) {
      l++;
    }
  }
};
```

```go

func moveZeroes(nums []int) {
	l := 0

	for r := 0; r < len(nums); r++ {
		if nums[l] == 0 {
			nums[l], nums[r] = nums[r], nums[l]
		}

		if nums[l] != 0 {
			l++
		}
	}
}

```
