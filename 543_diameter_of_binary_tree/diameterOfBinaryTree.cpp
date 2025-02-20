/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
    int maxDiameter = 0;

    int dfs(TreeNode* root) {
        if (root) {
            int left = dfs(root->left);
            int right = dfs(root->right);

            maxDiameter = max(maxDiameter, left + right);
            return max(left, right) + 1;
        }
        return 0;
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);

        return maxDiameter;
    }
};