function majorityElement(nums: number[]): number {
  const n = nums.length;
  nums.sort((a, b) => a - b);

  const mid = Math.floor(n / 2);

  return nums[mid];
}
