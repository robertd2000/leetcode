# [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14)

Given the `root` of a binary tree, return _the sum of all left leaves_.

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

## Example 1:

![alt text](image.png)

```
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
```

## Example 2:

```
Input: root = [1]
Output: 0
```

## Constraints:

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`

# Complexity

- **Time complexity:**
  `O(n)`

- **Space complexity:**
  `O(n)`

# Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        res = 0

        while stack:
            current, is_left = stack.pop()
            if not current:
                continue
            if not current.left and not current.right:
                if is_left:
                    res += current.val
            else:
                stack.append((current.left, True))
                stack.append((current.right, False))

        return res

```
