function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  let head = root;

  while (head) {
    if (p.val > head.val && q.val > head.val) {
      head = head.right;
    } else if (p.val < head.val && q.val < head.val) {
      head = head.left;
    } else {
      return head;
    }
  }
}
