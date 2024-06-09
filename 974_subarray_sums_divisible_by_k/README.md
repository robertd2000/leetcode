# [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/?envType=daily-question&envId=2024-06-09)

Given an integer array `nums` and an integer `k`, return _the number of non-empty subarrays that have a sum divisible by `k`_.

A `subarray` is a `contiguous` part of an array.

## Example 1:

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

## Example 2:

```
Input: nums = [5], k = 9
Output: 0
```

## Constraints:

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

# Code

```python

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [1] + [0] * k
        s = 0
        res = 0

        for num in nums:
            s = (s + num) % k
            res += count[s]
            count[s] += 1


        return res

```

```java

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] count = new int[k];
        count[0] = 1;

        int res = 0;
        int sum = 0;

        for (int num : nums) {
            sum = (sum + num) % k;
            if (sum < 0) sum += k;
            res += count[sum]++;
        }

        return res;
    }
}

```

```ts
function subarraysDivByK(nums: number[], k: number): number {
  const map = {
    0: 1,
  };

  let count = 0;
  let sum = 0;

  for (let i of nums) {
    sum = (sum + i) % k;

    if (sum < 0) sum += k;

    count += map[sum] || 0;
    map[sum] = map[sum] ? map[sum] + 1 : 1;
  }

  return count;
}
```
