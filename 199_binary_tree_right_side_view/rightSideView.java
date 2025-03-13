/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();

        dfs(root, 0, res);

        return res;
    }

    private void dfs(TreeNode root, int level, List<Integer> res) {
        if (root == null)
            return;

        if (res.size() <= level)
            res.add(root.val);

        res.set(level, root.val);

        dfs(root.left, level + 1, res);
        dfs(root.right, level + 1, res);
    }
}