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
        