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

**Linear time**

```py

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

```

```ts
function majorityElement(nums: number[]): number {
  let count = 0;
  let candidate = 0;

  for (let num of nums) {
    if (count === 0) {
      candidate = num;
    }

    if (num === candidate) {
      count++;
    } else {
      count--;
    }
  }

  return candidate;
}
```

**Sort**

```python

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        nums.sort()

        return nums[mid]

```

```ts
function majorityElement(nums: number[]): number {
  const n = nums.length;

  nums.sort((a, b) => a - b);

  const mid = Math.floor(n / 2);

  return nums[mid];
}
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

```cpp

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = nums[0];
        int count = 1;

        for (int i = 1; i < nums.size(); i++) {
            if (count == 0) {
                major = nums[i];
                count++;
            } else if (nums[i] == major) {
                count++;
            } else {
                count--;
            }
        }

        return major;
    }
};

```

```go

func majorityElement(nums []int) int {
    count := 1
    major := nums[0]

    for _, num := range nums[1:] {
        if count == 0 {
            count = 1
            major = num
        } else if num == major {
            count++
        } else {
            count--
        }
    }

    return major
}

```
