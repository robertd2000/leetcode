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

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  const stack: (TreeNode | null)[] = [];

  let left: TreeNode | null = null;
  let right: TreeNode | null = null;

  if (root.left) {
    if (!root.right) {
      return false;
    }

    stack.push(root.left);
    stack.push(root.right);
  } else if (root.right) {
    return false;
  }

  while (stack.length) {
    if (stack.length % 2 !== 0) return false;

    right = stack.pop();
    left = stack.pop();

    if (left.val !== right.val) return false;

    if (left.left) {
      if (!right.right) {
        return false;
      }

      stack.push(left.left);
      stack.push(right.right);
    } else if (right.right) {
      return false;
    }

    if (left.right) {
      if (!right.left) {
        return false;
      }

      stack.push(left.right);
      stack.push(right.left);
    } else if (right.left) {
      return false;
    }
  }
  return true;
}
