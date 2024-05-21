# [78. Subsets](https://leetcode.com/problems/subsets/description/?envType=daily-question&envId=2024-05-21)

Given an integer array `nums` of **unique** elements, return _all possible subsets (the power set)._

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

## Example 1:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

## Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints:

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

# Code

```python

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in sorted(nums):
            res += [item + [i] for item in res]

        return res

```
