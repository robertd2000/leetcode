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