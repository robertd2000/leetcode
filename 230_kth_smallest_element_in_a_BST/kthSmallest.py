from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = root
        stack = []

        while temp:
            stack.append(temp)
            temp = temp.left

        while k != 0:
            n = stack.pop()
            k -= 1

            if k == 0:
                return n.val

            r = n.right
            while r:
                stack.append(r)
                r = r.left

        return -1