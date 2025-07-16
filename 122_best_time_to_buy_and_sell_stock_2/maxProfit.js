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
