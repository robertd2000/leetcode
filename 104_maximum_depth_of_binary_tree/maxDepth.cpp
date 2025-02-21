/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int depth = 0;

    int dfs(TreeNode* root) {
        if (root) {
            int left = dfs(root->left);
            int right = dfs(root->right);
            int d = max(left, right) + 1;
            depth = max(depth, d);
            return d;
        }

        return 0;
    }
public:
    int maxDepth(TreeNode* root) {
        dfs(root);

        return depth;
    }
};