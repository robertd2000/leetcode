impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut cur = prices.get(0).copied().unwrap();

        for &p in prices.iter() {
            if p > cur {
                res += p - cur;
            }

            cur = p;
        }
        res as i32
    }
}