class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int pre = 1;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            res.push_back(pre);
            pre *= nums[i];
        }

        int post = 1;

        for (int i = n - 1; i >= 0; i--) {
            res[i] *= post;
            post *= nums[i];
        }

        return res;
    }
};