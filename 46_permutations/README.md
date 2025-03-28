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

```go

func permute(nums []int) [][]int {
    answer := make([][]int, 0)
    aux(&answer, 0, nums)
	return answer
}

func aux(answer *[][]int, idx int, nums []int) {
    if idx == len(nums) {
        c := make([]int, len(nums))
        copy(c, nums)
        *answer = append(*answer, c)
        return
    }
    for i := idx; i < len(nums); i++ {
        nums[idx], nums[i] = nums[i], nums[idx]
        aux(answer, idx + 1, nums)
        nums[i], nums[idx] = nums[idx], nums[i]
    }
    return
}

```

```java

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, List<Integer> path, List<List<Integer>> res) {
        if (nums.length == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            int[] newNums = new int[nums.length - 1];
            System.arraycopy(nums, 0, newNums, 0, i);
            System.arraycopy(nums, i + 1, newNums, i, nums.length - i - 1);

            path.add(nums[i]);

            dfs(newNums, path, res);

            path.remove(path.size() - 1);
        }
    }
}

```
