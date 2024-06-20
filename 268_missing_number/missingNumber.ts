function missingNumber(nums: number[]): number {
  let n = nums.length;
  let m = n + 1;

  let currentSum = nums.reduce((a, c) => (a += c), 0);
  let sum = (n * m) / 2;

  return sum - currentSum;
}
