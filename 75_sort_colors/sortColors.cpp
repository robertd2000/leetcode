class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0, 0, 0};
        int n = nums.size();

        for (int num : nums) {
            count[num]++;
        }

        int k = 0;

        for (int i = 0; i < sizeof(count)/sizeof(*count); i++) {
            for (int j = 0; j < count[i]; j++) {
                nums[k] = i;
                k++;
            }
        }

        return;
    }
};