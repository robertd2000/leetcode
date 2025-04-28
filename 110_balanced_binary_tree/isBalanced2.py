# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ERR_CODE = -sys.maxsize - 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._get_height(root) != ERR_CODE

    def _get_height(self, root: TreeNode) -> int:
        if root:
            left = self._get_height(root.left)
            if left == ERR_CODE:
                return ERR_CODE
            right = self._get_height(root.right)
            if right == ERR_CODE:
                return ERR_CODE
            diff = abs(left - right)
            if diff > 1:
                return ERR_CODE
            return max(left, right) + 1

        return 0
