/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let isNegative = false;

  if (x < 0) {
    isNegative = true;
    x = -x;
  }

  let res = 0;

  while (x > 0) {
    let digit = x % 10;
    x = Math.floor(x / 10);

    if (
      res > Math.floor((2 ** 31 - 1) / 10) ||
      (res === Math.floor((2 ** 31 - 1) / 10) && digit > 7)
    ) {
      return 0;
    }

    res = res * 10 + digit;
  }

  return isNegative ? -res : res;
};
