# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        self.dfs(root, 0, res)

        return res
        
    def dfs(self, root: Optional[TreeNode], level: int, res: List[int]):
        if root:
            if len(res) <= level:
                res.append(root.val)
            res[level] = root.val
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)
                
        return