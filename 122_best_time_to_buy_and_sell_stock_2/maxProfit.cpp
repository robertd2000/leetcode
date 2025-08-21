class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int curr = prices[0];

        for (const int& price : prices) {
            if (price < curr) {
                curr = price;
            } else {
                profit += price - curr;
                curr = price;
            }
        }

        return profit;
    }
};