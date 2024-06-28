class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -pow(2, 31) - 1, pow(2, 31) + 1)

    def dfs(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if root is None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.dfs(root.left, minVal, root.val) and self.dfs(
            root.right, root.val, maxVal
        )