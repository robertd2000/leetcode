function minMoves2(nums: number[]): number {
  nums.sort((a, b) => a - b);

  const n = nums.length;
  const midIdx = Math.floor(n / 2);
  const mid = nums[midIdx];

  let res = 0;

  for (let num of nums) {
    res += Math.abs(mid - num);
  }

  return res;
}
