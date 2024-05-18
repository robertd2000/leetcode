# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        if root.left:
            res += self.distributeCoins(root.left)
            root.val += root.left.val - 1
            res += abs(root.left.val - 1)
        if root.right:
            res += self.distributeCoins(root.right)
            root.val += root.right.val - 1
            res += abs(root.right.val - 1)
        return res