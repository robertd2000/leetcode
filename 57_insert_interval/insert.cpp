class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        for (int i = 0; i < intervals.size(); i++) {
            vector<int> interval = intervals[i];

            if (newInterval[1] < interval[0]) {
                res.push_back(newInterval);
                res.insert(res.end(), intervals.begin() + i, intervals.end());
                return res;
            } else if (newInterval[0] > interval[1]) {
                res.push_back(interval);
            } else {
                int start = min(newInterval[0], interval[0]);
                int end = max(newInterval[1], interval[1]);
                newInterval = {start, end};
            }
        }

        res.push_back(newInterval);

        return res;
    }
};