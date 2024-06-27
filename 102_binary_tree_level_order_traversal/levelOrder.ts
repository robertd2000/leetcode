function levelOrder(root: TreeNode | null): number[][] {
  if (root === null) return [];

  let queue = [root];
  let levels = [];
  const result: number[][] = [[root.val]];

  while (queue.length) {
    const current = queue.shift();

    if (current.left) {
      levels.push(current.left);
    }

    if (current.right) {
      levels.push(current.right);
    }

    if (!queue.length) {
      if (levels.length) {
        result.push(levels.map((n) => n.val));
      }
      queue = levels;
      levels = [];
    }
  }

  return result;
}
