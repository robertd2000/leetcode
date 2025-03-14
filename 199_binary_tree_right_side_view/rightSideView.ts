/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function rightSideView(root: TreeNode | null): number[] {
  const res = [];

  dfs(root, 0, res);

  return res;
}

function dfs(root: TreeNode | null, level: number, res: number[]) {
  if (root) {
    if (res.length <= level) res.push(root.val);

    res[level] = root.val;

    dfs(root.left, level + 1, res);
    dfs(root.right, level + 1, res);
  }
}
