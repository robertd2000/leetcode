/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  const n = nums.length;

  if (n === k) return;

  let right = k % n;

  reverse(nums, 0, n - 1);
  reverse(nums, 0, right - 1);
  reverse(nums, right, n - 1);
}

function reverse(nums: number[], start: number, end: number): void {
  while (start < end) {
    let temp = nums[start];
    nums[start] = nums[end];
    nums[end] = temp;
    start++;
    end--;
  }
}
