function checkSubarraySum(nums: number[], k: number): boolean {
  let cumulative = 0;

  const map = { "0": -1 };

  for (let i = 0; i < nums.length; i++) {
    cumulative += nums[i];

    if (map[cumulative % k] === undefined) {
      map[cumulative % k] = i;
    }

    if (map[cumulative % k] < i - 1) {
      return true;
    }
  }

  return false;
}
