/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  const n = nums.length;
  k = k % n;

  if (n === 1 || k === 0) {
    return;
  }

  const temp = [...nums];

  for (let i = 0; i < k + 1; i++) {
    nums[i] = temp[i + n - k];
  }

  for (let i = k; i < n; i++) {
    nums[i] = temp[i - k];
  }
}
