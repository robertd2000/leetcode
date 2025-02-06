#include <vector>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int current_min = prices[0];

        for (int price : prices) {
            int profit = price - current_min;
            current_min = min(current_min, price);
            max_profit = max(max_profit, profit);
        }

        return max_profit;
    }
};