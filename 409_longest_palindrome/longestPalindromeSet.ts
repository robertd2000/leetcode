function longestPalindrome(s: string): number {
  const seen = new Set();

  let res = 0;

  for (let c of s) {
    if (seen.has(c)) {
      res += 2;
      seen.delete(c);
    } else {
      seen.add(c);
    }
  }

  if (seen.size) {
    res += 1;
  }

  return res;
}
