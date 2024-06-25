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

function isBalanced(root: TreeNode | null): boolean {
  if (root === null) return true;

  const left = getHeight(root.left);
  const right = getHeight(root.right);

  const skew = Math.abs(left - right);

  return skew <= 1 && isBalanced(root.left) && isBalanced(root.right);
}

function getHeight(root: TreeNode | null): number {
  if (root === null) return 0;

  const leftHeight = getHeight(root.left);
  const rightHeight = getHeight(root.right);

  return Math.max(leftHeight, rightHeight) + 1;
}
