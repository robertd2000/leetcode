# [260. Single Number III](https://leetcode.com/problems/single-number-iii/description/?envType=daily-question&envId=2024-05-31)

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

## Example 1:

```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
```

## Example 2:

```
Input: nums = [-1,0]
Output: [-1,0]
```

## Example 3:

```
Input: nums = [0,1]
Output: [1,0]
```

## Constraints:

- `2 <= nums.length <= 3 * 10^4`
- -`2^31 <= nums[i] <= 2^31 - 1`
- Each integer in nums will appear twice, only two integers will appear once.

# Code

**Hash table**

```python

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash = {}

        res = []

        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1

        for key, item in hash.items():
            if item == 1:
                res.append(key)
        return res

```

```java

class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int[] result = new int[] { 0, 0 };

        for (int i = 0; i < nums.length; i++) {
            int value = map.getOrDefault(nums[i], 0);
            map.put(nums[i], ++value);
        }
        int idx = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (value == 1 && idx < 2) {
                result[idx] = key;
                idx++;
            }
        }
        return result;
    }
}

```
