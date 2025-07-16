/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  const map = new Map();

  const res = [];

  for (let num of nums1) {
    const val = map.get(num) || 0;
    map.set(num, val + 1);
  }

  for (let num of nums2) {
    if (map.has(num) && map.get(num) > 0) {
      res.push(num);
      map.set(num, map.get(num) - 1);
    }
  }

  return res;
};
