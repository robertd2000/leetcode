# [623. Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/description/?envType=daily-question&envId=2024-04-16/)

Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the `root` node is at depth `1`.

The adding rule is:

- Given the integer `depth`, for each not null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root.
- `cur`'s original left subtree should be the left subtree of the new left subtree root.
- `cur`'s original right subtree should be the right subtree of the new right subtree root.
- If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

## Example 1:

![Example 1](image.png)

```
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
```

## Example 2:

![Example 2](image-1.png)

```
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
```

## Constraints:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- The depth of the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`
- `-105 <= val <= 105`
- `1 <= depth <= the depth of tree + 1`

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(1)`

# Code

**Recursive**

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        return self.add(root, val, depth, 1)

    def add(self, root: Optional[TreeNode], val: int, depth: int, current: int) -> Optional[TreeNode]:
        if not root:
            return None
        if current == depth - 1:
            l, r = root.left, root.right
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = l
            root.right.right = r

            return root

        root.left = self.add(root.left, val, depth, current + 1)
        root.right = self.add(root.right, val, depth, current + 1)
        return root

```
