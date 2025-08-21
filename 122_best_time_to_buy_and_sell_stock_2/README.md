# [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return _the **maximum** profit you can achieve_.

## Example 1:

```

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

```

## Example 2:

```

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

```

## Example 3:

```

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

```

Нам нужно найти момент, когда цена минимальна и когда цена максимальна (относительно).
Сохраняем текущий минимум в `curr`. Проходимся в цикле по массиву и если текущий элемент меньше текущего минимума, то обновляем текущий минимум. Иначе, получается мы можем продать нашу акцию и получить выгоду, т.к. мы ее купили дешевле. Значит к `profit` прибавим разницу между текущей ценой акции и текущим минимумом, за который мы ее купили. Также обновим текущий минимум.

## Constraints:

- `1 <= prices.length <= 3 * 104`
- `0 <= prices[i] <= 104`

```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let curr = prices[0];
  let profit = 0;

  for (let price of prices) {
    if (price < curr) {
      curr = price;
    } else {
      profit += price - curr;
      curr = price;
    }
  }

  return profit;
};
```

```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]

        return res

```

```java

class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] < prices[i]) {
                res += prices[i] - prices[i - 1];
            }
        }

        return res;
    }
}

```

```cpp
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
```
