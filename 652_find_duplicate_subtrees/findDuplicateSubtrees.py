# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        ans = []
        count = collections.Counter()

        def encode(root: Optional[TreeNode]) -> str:
            if not root:
                return ""

            encoded = str(root.val) + "#" + encode(root.left) + "#" + encode(root.right)
            count[encoded] += 1
            if count[encoded] == 2:
                ans.append(root)
            return encoded

        encode(root)
        return ans