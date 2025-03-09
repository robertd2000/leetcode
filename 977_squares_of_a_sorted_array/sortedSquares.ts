function sortedSquares(nums: number[]): number[] {
  const n = nums.length;
  const res = Array(n).fill(0);

  let l = 0;
  let r = n - 1;

  for (let i = n - 1; i >= 0; i--) {
    let val = 0;

    if (Math.abs(nums[l]) > Math.abs(nums[r])) {
      val = nums[l];
      l++;
    } else {
      val = nums[r];
      r--;
    }

    res[i] = val ** 2;
  }

  return res;
}
