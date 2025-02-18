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
public:
    bool isBalanced(TreeNode* root) {
        if (root) {
            int left = getHeight(root->left);
            int right = getHeight(root->right);
            int skew = abs(left - right);

            if (!isBalanced(root->left)) return false;
            if (!isBalanced(root->right)) return false;
            if (skew > 1) return false;

            return true;
        }
        return true;
    }

    int getHeight(TreeNode* root) {
        if (root == 0) return 0;

        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);

        return max(leftHeight, rightHeight) + 1;
    }
};