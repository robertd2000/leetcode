/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const res = [];

  dfs(root, 0, res);
  return res;
};

function dfs(root, level, res) {
  if (root) {
    if (res.length <= level) {
      res.push([]);
    }

    res[level].push(root.val);
    dfs(root.left, level + 1, res);
    dfs(root.right, level + 1, res);
  }

  return;
}
