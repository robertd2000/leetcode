function myAtoi(s: string): number {
  let i = 0;
  const n = s.length;
  let res = 0;
  let sign = 1;

  while (i < n && s[i] === " ") i++;

  if (i < n && (s[i] === "-" || s[i] === "+")) {
    if (s[i] === "-") sign = -1;
    if (s[i] === "+") sign = 1;
    i++;
  }

  while (i < n && s[i] >= "0" && s[i] <= "9") {
    res = res * 10 + (s[i].charCodeAt(0) - "0".charCodeAt(0));
    if (res * sign > 2 ** 31 - 1) return 2 ** 31 - 1;
    if (res * sign < -(2 ** 31)) return -(2 ** 31);
    i++;
  }

  return res * sign;
}
