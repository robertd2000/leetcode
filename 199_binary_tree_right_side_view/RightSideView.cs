/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> RightSideView(TreeNode root) {
        IList<int> res = new List<int>();

        Dfs(root, 1, res);

        return res;
    }

    private void Dfs(TreeNode root, int level, IList<int> res) {
        if (root != null) {
            if (res.Count < level) {
                res.Add(root.val);
            }

            Dfs(root.right, level + 1, res);
            Dfs(root.left, level + 1, res);
        }
    }
}