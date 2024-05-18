# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root: Optional[TreeNode]):
        if root == None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res +=  abs(left) + abs(right)
        return root.val + left + right - 1