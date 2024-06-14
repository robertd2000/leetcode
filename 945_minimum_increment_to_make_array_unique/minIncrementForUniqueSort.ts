function minIncrementForUnique(nums: number[]): number {
  nums.sort((a, b) => a - b);

  let count = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] >= nums[i + 1]) {
      count += nums[i] + 1 - nums[i + 1];
      nums[i + 1] = nums[i] + 1;
    }
  }

  return count;
}
