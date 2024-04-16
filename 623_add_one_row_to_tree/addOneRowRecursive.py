# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        return self.add(root, val, depth, 1)

    def add(self, root: Optional[TreeNode], val: int, depth: int, current: int) -> Optional[TreeNode]:
        if not root:
            return None
        if current == depth - 1:
            l, r = root.left, root.right
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = l 
            root.right.right = r

            return root

        root.left = self.add(root.left, val, depth, current + 1)
        root.right = self.add(root.right, val, depth, current + 1)
        return root