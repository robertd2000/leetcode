# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        stack = [(root, 0)]

        while stack:
            root, current = stack.pop()
            current = current * 10 + root.val
            if not root.left and not root.right:
                res += current
            if root.left:
                stack.append((root.left, current))
            if root.right:
                stack.append((root.right, current))

        return res
