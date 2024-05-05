# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

Given an integer array `nums`, return _an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except_ `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Example 1:

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

## Example 2:

```
nput: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints:

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(1)`

# Code

```python

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        n = len(nums)
        pre = 1
        post = 1

        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
            res[n - i - 1] *= post
            post *= nums[n - i - 1]

        return res

```

```java

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int prefix = 1;
        int postfix = 1;

        Arrays.fill(result, 1);

        for (int i = 0; i < n; i++) {
            result[i] *= prefix;
            prefix *= nums[i];

            result[n - i - 1] *= postfix;
            postfix *= nums[n - i - 1];
        }

        return result;
    }
}

```
