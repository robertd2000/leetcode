var myAtoi = function (s) {
  let i = 0,
    n = s.length,
    sign = 1,
    result = 0;

  while (i < n && s[i] === " ") i++;

  if (i < n && (s[i] === "+" || s[i] === "-")) {
    sign = s[i] === "-" ? -1 : 1;
    i++;
  }

  while (i < n && s[i] >= "0" && s[i] <= "9") {
    result = result * 10 + (s[i].charCodeAt(0) - "0".charCodeAt(0));
    if (result * sign > 2 ** 31 - 1) return 2 ** 31 - 1;
    if (result * sign < -(2 ** 31)) return -(2 ** 31);
    i++;
  }

  return result * sign;
};
