# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            left = self.removeLeafNodes(root.left, target)
            root.left = left
        if root.right:    
            right = self.removeLeafNodes(root.right, target)
            root.right = right

        if root.val == target and root.left == root.right:
            return None
        else:
            return root   

        return root