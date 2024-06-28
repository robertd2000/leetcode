function isValidBST(root: TreeNode | null): boolean {
  return dfs(root, -Infinity, Infinity);
}

function dfs(root: TreeNode | null, minVal: number, maxVal: number) {
  if (root == null) return true;

  if (root.val <= minVal || root.val >= maxVal) return false;

  return dfs(root.left, minVal, root.val) && dfs(root.right, root.val, maxVal);
}
