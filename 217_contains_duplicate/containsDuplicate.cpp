class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> counter;

        for (int num : nums) {
            if (counter.find(num) != counter.end()) return true;
            counter[num] = true;
        }
        
        return false;
    }
};