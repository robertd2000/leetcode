# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            left = self.getHeight(root.left, 0)
            right = self.getHeight(root.right, 0)

            skew = abs(left - right)

            return skew <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 

        return True

        
    def getHeight(self, root, height):
        if not root:
            return 0
        lHeight = self.getHeight(root.left, height)
        rHeight = self.getHeight(root.right, height)

        return max(lHeight, rHeight) + 1
        