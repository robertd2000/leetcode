[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

**Example 1:**

![alt text](image.png)

Input: root = [3,1,4,null,2], k = 1
Output: 1

**Example 2:**

![alt text](image-1.png)

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

**Constraints:**

- The number of nodes in the tree is n.
- 1 <= k <= n <= 104
- 0 <= Node.val <= 104

**Follow up**: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

```py

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

```
