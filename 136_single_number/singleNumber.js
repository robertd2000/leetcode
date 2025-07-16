/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const set = new Set(nums);
  const fullSum = Array.from(set).reduce((acc, cur) => (acc += cur), 0) * 2;
  const actualSum = nums.reduce((acc, cur) => (acc += cur), 0);

  return fullSum - actualSum;
};
