class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function kthSmallest(root: TreeNode | null, k: number): number {
  const stack: TreeNode[] = [];

  while (root) {
    stack.push(root);
    root = root.left;
  }

  while (k !== 0) {
    const n = stack.pop() as TreeNode;

    k -= 1;

    if (k === 0) return n.val;

    let r = n.right;

    while (r) {
      stack.push(r);
      r = r.left;
    }
  }

  return -1;
}
