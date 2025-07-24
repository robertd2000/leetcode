/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  let n = haystack.length;
  let m = needle.length;

  for (let i = 0; i < n - m + 1; i++) {
    if (haystack.slice(i, i + m) === needle) return i;
  }

  return -1;
};
