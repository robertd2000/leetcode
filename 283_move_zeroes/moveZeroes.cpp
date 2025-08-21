#include <vector>
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l = 0;

        for (int r = 0; r < nums.size(); r++) {
            if (nums[l] == 0) {
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
            }
            if (nums[l] != 0)
                l++;
        }
    }
};