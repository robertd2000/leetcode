# [137. Single Number II](https://leetcode.com/problems/single-number-ii/description/)

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

**Input:** nums = [2,2,3,2]
**Output:** 3

**Example 2:**

**Input:** nums = [0,1,0,1,0,1,99]
**Output:** 99

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `-231 <= nums[i] <= 231 - 1`
- Each element in `nums` appears exactly **three times** except for one element which appears **once**.

# Code

```python

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            if value == 1:
                return key

```

```python
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            ans |= bit_sum << i

        if ans >= 2**31:
            ans -= 2**32

        return ans
```

```python
class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones
```

```ts
function singleNumber(nums: number[]): number {
  const map = {};

  for (let num of nums) {
    const value = map[num];
    if (value) {
      map[num] = value + 1;
    } else {
      map[num] = 1;
    }
  }

  for (const [key, value] of Object.entries(map)) {
    if (value == 1) {
      return +key;
    }
  }

  return 0;
}
```
