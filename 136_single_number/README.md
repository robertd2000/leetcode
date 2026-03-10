# [136. Single Number](https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75)

Given a **non-empty** array of integers `nums`, every element appears _twice_ except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Example 1:

```
Input: nums = [2,2,1]
Output: 1
```

## Example 2:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

## Example 3:

```
Input: nums = [1]
Output: 1

```

## Constraints:

- `1 <= nums.length <= 3 * 104`
- `-3 * 104 <= nums[i] <= 3 * 104`
- Each element in the array appears twice except for one element which appears only once.

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        for key, value in hash.items():
            if value == 1:
                return key

```

```ts
function singleNumber(nums: number[]): number {
  let result = 0;

  for (let num of nums) {
    result ^= num;
  }

  return result;
}
```

```ts
function singleNumber(nums: number[]): number {
  const n = nums.length;

  const map = {};

  for (let num of nums) {
    if (num in map) {
      map[num]++;
    } else {
      map[num] = 1;
    }
  }

  for (let [key, value] of Object.entries(map)) {
    if (value == 1) {
      return +key;
    }
  }

  return 0;
}
```

```go

package singlenumber

func singleNumber(nums []int) int {
	unique := getUnique(nums)
	currSum := sum(nums)
	uniqueSum := sum(unique)

	return uniqueSum*2 - currSum
}

func sum(nums []int) int {
	s := 0

	for _, num := range nums {
		s += num
	}

	return s
}

func getUnique(nums []int) []int {
	res := make([]int, 0)
	set := make(map[int]bool)

	for _, num := range nums {
		if _, ok := set[num]; !ok {
			res = append(res, num)
		}

		set[num] = true
	}

	return res
}

```

```rs

use std::collections::HashMap;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let unique = get_unique(&nums);
        let curr_sum = sum(&nums);
        let unique_sum = sum(&unique);

        unique_sum * 2 - curr_sum
    }
}

fn sum(nums: &Vec<i32>) -> i32 {
    let mut sum = 0;

    for &v in nums {
        sum += v;
    }

    sum
}

fn get_unique(nums: &Vec<i32>) -> Vec<i32> {
        let mut h_map = HashMap::new();
        let mut res = Vec::new();

        for &v in nums {
            match h_map.get(&v) {
                Some(_) => (),
                _ => {
                    h_map.insert(v, true);
                    res.push(v);
                }
            }
        }

        res
}

```

```rs

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        nums.iter().fold(0, |acc, x| acc ^ x)
    }
}

```

```rs

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for &num in nums.iter() {
            result ^= num;
        }
        return result;
    }
}

```
