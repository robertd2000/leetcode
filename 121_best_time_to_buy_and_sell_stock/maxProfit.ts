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
