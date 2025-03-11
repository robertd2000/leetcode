/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  const n = nums.length;
  let l = 0;
  let r = n - 1;

  while (l <= r) {
    let m = l + Math.floor((r - l) / 2);

    if (nums[m] < target) {
      l = m + 1;
    } else if (nums[m] > target) {
      r = m - 1;
    } else {
      return m;
    }
  }

  return -1;
};
