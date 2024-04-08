class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;

        int max = findMax(candies);

        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= max) {
                result.push_back(true);
            } else {
                result.push_back(false);
            }
        } 

        return result;
    }

    int findMax(vector<int>& list) {
        int max = 0;

        for (int i = 0; i < list.size(); i++) {
            if (list[i] > max) {
                max = list[i];
            }
        }

        return max;
    }
};