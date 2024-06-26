class Solution:
    maxDiameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.maxDiameter = max(self.maxDiameter, left + right)
            return max(left, right) + 1

        dfs(root)

        return self.maxDiameter