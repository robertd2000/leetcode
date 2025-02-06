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