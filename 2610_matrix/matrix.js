/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function (nums) {
  const freq = Array(nums.length + 1).fill(0);
  const res = [];

  nums.forEach((i) => {
    if (freq[i] >= res.length) {
      res.push([]);
    }

    res[freq[i]].push(i);
    freq[i]++;
  });

  return res;
};
