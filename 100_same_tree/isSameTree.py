# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            n, m = stack.pop()

            if not n and not m:
                continue
            elif None in [n, m]:
                return False
            else:
                if n.val != m.val:
                    return False
                stack.append((n.right, m.right))
                stack.append((n.left, m.left))

        return True