# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode], current: int):
            if not root:
                return 0
            current = current * 10 + root.val
            if not root.left and not root.right:
                return current
            return traverse(root.left, current) + traverse(root.right, current)

        return traverse(root, 0)