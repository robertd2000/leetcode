[199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1:**

**Input**
Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

![alt text](image.png)

**Example 1:**

**Input**
Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

![alt text](image-1.png)

**Constraints:**

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

```py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        self.dfs(root, 0, res)

        return res

    def dfs(self, root: Optional[TreeNode], level: int, res: List[int]):
        if root:
            if len(res) <= level:
                res.append(root.val)
            res[level] = root.val
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

        return

```

```java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();

        dfs(root, 0, res);

        return res;
    }

    private void dfs(TreeNode root, int level, List<Integer> res) {
        if (root == null)
            return;

        if (res.size() <= level)
            res.add(root.val);

        res.set(level, root.val);

        dfs(root.left, level + 1, res);
        dfs(root.right, level + 1, res);
    }
}

```
