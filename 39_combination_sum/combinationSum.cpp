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