# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode], is_left: bool):
            if root:
                traverse(root.left, True)
                traverse(root.right, False)
                if not root.left and not root.right:  
                    if is_left:
                        self.res += root.val
        
        traverse(root, False)

        return self.res