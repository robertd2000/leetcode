/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let sum = 0;
  let maxSum = nums[0];

  for (let num of nums) {
    if (sum < 0) sum = 0;
    sum += num;
    maxSum = Math.max(maxSum, sum);
  }

  return maxSum;
};
