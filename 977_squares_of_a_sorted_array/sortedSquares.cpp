class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            int n = nums.size();
            vector<int> res(n);
            int l = 0;
            int r = n - 1;
    
            for (int i = n - 1; i >= 0; i--) {
                int val = 0;
                if (abs(nums[l]) > abs(nums[r])) {
                    val = nums[l];
                    l++;
                } else {
                    val = nums[r];
                    r--;
                }
                res[i] = pow(val, 2);
            }
    
            return res;
        }
    };