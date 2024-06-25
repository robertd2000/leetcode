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

  let balanced = true;

  function getHeight(root: TreeNode | null): number {
    if (root === null) return 0;

    const leftHeight = getHeight(root.left);

    if (balanced === false) {
      return 0;
    }
    const rightHeight = getHeight(root.right);

    const skew = Math.abs(leftHeight - rightHeight);

    if (skew > 1) {
      balanced = false;
      return 0;
    }
    return Math.max(leftHeight, rightHeight) + 1;
  }

  getHeight(root);

  return balanced;
}
