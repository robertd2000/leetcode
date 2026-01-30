[652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/description/)

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

**Example 1:**

![alt text](image.png)

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

**Example 2:**

![alt text](image-1.png)
Input: root = [2,1,1]
Output: [[1]]

**Example 3:**

![alt text](image-2.png)
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

**Constraints:**

- The number of the nodes in the tree will be in the range `[1, 5000]`
- `-200 <= Node.val <= 200`

## Code
