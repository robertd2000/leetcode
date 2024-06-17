function isPalindrome(x: number): boolean {
  const s = x.toString();
  const r = s.split("").reverse().join("");

  return s === r;
}
