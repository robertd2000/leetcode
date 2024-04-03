class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<int> frequency(nums.size() + 1);
        vector<vector<int>> result;

        for (int i : nums) {
            if (frequency[i] >= result.size()) {
                result.push_back({});
            }

            result[frequency[i]].push_back(i);
            frequency[i]++;
        }

        return result;
    }
};