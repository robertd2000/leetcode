# [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

## Example 1:

```

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

```

## Example 2:

```

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

```

## Example 3:

```

Input: candidates = [2], target = 1
Output: []

```

## Constraints:

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of candidates are distinct.
- `1 <= target <= 40`

```py

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates: List[int], target: int, path: List[int], res: List[List[int]]):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for idx, candidate in enumerate(candidates):
            new_target = target - candidate
            new_path = path + [candidate]
            self.dfs(candidates[idx:], new_target, new_path, res)

```

```cpp

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;

        dfs(candidates, target, path, res);

        return res;
    }

    void dfs(vector<int> candidates, int target, vector<int>& path, vector<vector<int>>& res) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
        }

        for (int i = 0; i < candidates.size(); i++) {
            int new_target = target - candidates[i];
            vector<int> new_path = path;
            new_path.push_back(candidates[i]);
            dfs(vector<int>(candidates.begin() + i, candidates.end()), new_target, new_path, res);
        }
    }
};

```

```java

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();

        dfs(candidates, target, path, res);

        return res;
    }

    private void dfs(int[] candidates, int target, List<Integer> path, List<List<Integer>> res) {
        if (target < 0) return;
        if (target == 0) {
            res.add(path);
            return;
        }
        for (int i = 0; i < candidates.length; i++) {
            int newTarget = target - candidates[i];
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(candidates[i]);
            dfs(Arrays.copyOfRange(candidates, i, candidates.length), newTarget, newPath, res);
        }

    }
}

```
