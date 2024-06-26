function diameterOfBinaryTree(root: TreeNode | null): number {
  let max = 0;

  function getHeight(root: TreeNode | null): number {
    if (root === null) return 0;

    const left = root.left ? getHeight(root.left) : 0;
    const right = root.right ? getHeight(root.right) : 0;

    const diameter = left + right;
    max = Math.max(max, diameter);

    return Math.max(left, right) + 1;
  }

  getHeight(root);

  return max;
}
