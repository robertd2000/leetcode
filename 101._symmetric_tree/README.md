[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example 1:**

![alt text](image.png)

Input: root = [1,2,2,3,4,4,3]
Output: true

**Example 2:**

![alt text](image-1.png)

Input: root = [1,2,2,3,4,4,3]
Output: true

**Constraints:**

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-100 <= Node.val <= 100`

```py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left or not right:
            return left == right
        if not left.val == right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
```

```py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []

        left = None
        right = None

        if root.left:
            if not root.right:
                return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right:
            return False

        while stack:
            if len(stack) % 2 != 0:
                return False

            right = stack.pop()
            left = stack.pop()

            if left.val != right.val:
                return False

            if left.left:
                if not right.right:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right:
                return False

            if left.right:
                if not right.left:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left:
                return False

        return True

```

```ts
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

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  return dfs(root.left, root.right);
}

function dfs(left: TreeNode | null, right: TreeNode | null): boolean {
  if (!left || !right) {
    return left == right;
  }

  if (left.val != right.val) return false;

  return dfs(left.left, right.right) && dfs(left.right, right.left);
}
```
