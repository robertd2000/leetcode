use std::cmp;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = prices[0];

        for i in 1..prices.len() {
            let price = prices[i];
            let profit = price - min_price;
            max_profit = cmp::max(max_profit, profit);
            min_price = cmp::min(min_price, price);
        }

        return max_profit;
    }
}
