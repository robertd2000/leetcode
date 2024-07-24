/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const hashMap = new Map();
  const freq = new Array(nums.length + 1).fill(null);

  for (let num of nums) {
    if (hashMap.has(num)) {
      const value = hashMap.get(num) + 1;
      hashMap.set(num, value);
    } else {
      hashMap.set(num, 1);
    }
  }

  hashMap.forEach((value, key) => {
    if (Array.isArray(freq[value])) {
      freq[value].push(key);
    } else {
      freq[value] = [key];
    }
  });

  const result = [];

  for (let i = freq.length - 1; i >= 0; i--) {
    if (Array.isArray(freq[i]))
      for (let j of freq[i]) {
        result.push(j);
        if (result.length === k) return result;
      }
  }

  return result;
};
