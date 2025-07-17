# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

Given an integer array `nums`, find the **subarray** with the largest sum, and return _its sum_.

## Example 1:

```

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

## Example 2:

```

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

## Example 3:

```

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

## Constraints:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

```py

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

```

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let sum = 0;
  let maxSum = nums[0];

  for (let num of nums) {
    if (sum < 0) sum = 0;
    sum += num;
    maxSum = Math.max(maxSum, sum);
  }

  return maxSum;
};
```

```ts
function maxSubArray(nums: number[]): number {
  let max = nums[0];
  let sum = 0;

  for (let num of nums) {
    if (sum < 0) {
      sum = 0;
    }
    sum += num;
    max = Math.max(max, sum);
  }

  return max;
}
```

```go

func maxSubArray(nums []int) int {
    maxSum := nums[0]
    sum := 0

    for _, num := range nums {
        if sum < 0 {
            sum = 0
        }

        sum += num
        maxSum = max(maxSum, sum)
    }

    return maxSum
}

```

```java

class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int sum = 0;

        for (int num:nums) {
            if (sum < 0) sum = 0;
            sum += num;
            maxSum = Math.max(maxSum, sum);
        }

        return maxSum;
    }
}

```
