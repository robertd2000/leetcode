function maxDepth(root: TreeNode | null): number {
  return dfs(root);
}

function dfs(root: TreeNode | null): number {
  if (root === null) return 0;

  const left = dfs(root.left);
  const right = dfs(root.right);

  return Math.max(left, right) + 1;
}

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
