/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const n = nums.length;
  const r = k % n;

  reverse(nums, 0, n - 1);
  reverse(nums, 0, r - 1);
  reverse(nums, r, n - 1);
};

function reverse(nums, l, r) {
  while (l < r) {
    let temp = nums[l];
    nums[l] = nums[r];
    nums[r] = temp;
    l++;
    r--;
  }
}
