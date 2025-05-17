# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
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
