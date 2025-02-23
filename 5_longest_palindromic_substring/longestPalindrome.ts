function longestPalindrome(s: string): string {
  const n = s.length;

  let maxLen = 0;
  let res = "";

  for (let i = 0; i < n; i++) {
    let l = i;
    let r = i;

    while (l >= 0 && r < n && s[l] === s[r]) {
      let diff = r - l + 1;
      if (diff > maxLen) {
        maxLen = diff;
        res = s.slice(l, r + 1);
      }
      l -= 1;
      r += 1;
    }
    l = i;
    r = i + 1;

    while (l >= 0 && r < n && s[l] === s[r]) {
      let diff = r - l + 1;
      if (diff > maxLen) {
        maxLen = diff;
        res = s.slice(l, r + 1);
      }
      l -= 1;
      r += 1;
    }
  }

  return res;
}
