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