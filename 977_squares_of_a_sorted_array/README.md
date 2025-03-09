# [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/description/)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

## Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

# Code

```ts
function sortedSquares(nums: number[]): number[] {
  const n = nums.length;
  const res = Array(n).fill(0);

  let l = 0;
  let r = n - 1;

  for (let i = n - 1; i >= 0; i--) {
    let val = 0;

    if (Math.abs(nums[l]) > Math.abs(nums[r])) {
      val = nums[l];
      l++;
    } else {
      val = nums[r];
      r--;
    }

    res[i] = val ** 2;
  }

  return res;
}
```
