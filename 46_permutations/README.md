[46. Permutations](https://leetcode.com/problems/permutations/)

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Example 2:**

**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

**Example 3:**

**Input:** nums = [1]
**Output:** [[1]]

**Constraints:**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

```py

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: List[int], path: List[int] = [], res: List[List[int]] = []):
        if not nums:
            res.append(path[:])

        for i in range(len(nums)):
            newNums = nums[:i] + nums[i + 1:]
            path.append(nums[i])
            self.dfs(newNums, path, res)
            path.pop()
        return res

```

```ts
function permute(nums: number[]): number[][] {
  return dfs(nums, [], []);
}

function dfs(nums: number[], path: number[], res: number[][]) {
  const n = nums.length;

  if (n === 0) {
    res.push([...path]);
  }

  for (let i = 0; i < n; i++) {
    const newNums = [...nums.slice(0, i), ...nums.slice(i + 1)];
    path.push(nums[i]);
    dfs(newNums, path, res);
    path.pop();
  }

  return res;
}
```
