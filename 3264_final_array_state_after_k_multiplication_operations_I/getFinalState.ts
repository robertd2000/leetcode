function getFinalState(
  nums: number[],
  k: number,
  multiplier: number
): number[] {
  for (let i = 0; i < k; i++) {
    let idx = getMinIdx(nums);
    nums[idx] *= multiplier;
  }

  return nums;
}

function getMinIdx(nums: number[]): number {
  let min = nums[0];
  let idx = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < min) {
      min = nums[i];
      idx = i;
    }
  }

  return idx;
}
