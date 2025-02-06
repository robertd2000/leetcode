# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the _maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

## Example 1:

```

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

## Example 2:

```

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

```

## Constraints:

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit  = 0

        while r < len(prices):
            candidate = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_profit = max([candidate, max_profit ])
            else:
                l = r
            r += 1

        return max_profit

```

```cpp

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

```

```ts
function maxProfit(prices: number[]): number {
  let max = 0;
  let currentMin = prices[0];

  prices.forEach((price) => {
    const profit = price - currentMin;
    max = Math.max(max, profit);
    currentMin = Math.min(currentMin, price);
  });

  return max;
}
```
