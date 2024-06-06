# [1296. Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/)

Given an array of integers `nums` and a positive integer `k`, check whether it is possible to divide this array into sets of `k` consecutive numbers.

Return `true` _if it is possible_. Otherwise, return `false`.

## Example 1:

```
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
```

## Example 2:

```
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
```

## Example 3:

```
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
```

## Constraints:

- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

# Code

```ts
function isPossibleDivide(nums: number[], k: number): boolean {
  const n = nums.length;

  if (n % k !== 0) return false;

  const map = {};

  for (let i of nums) {
    map[i] = map[i] ? map[i] + 1 : 1;
  }

  nums.sort((a, b) => a - b);

  for (let i of nums) {
    if (map[i] === 0) continue;

    for (let j = 0; j < k; j++) {
      const curr = i + j;

      if (!map[curr]) {
        return false;
      }

      map[curr]--;
    }
  }

  return true;
}
```
