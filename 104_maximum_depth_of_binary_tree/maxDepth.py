class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return max(left, right) + 1

        return dfs(root)