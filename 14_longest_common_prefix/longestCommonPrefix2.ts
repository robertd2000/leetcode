function longestCommonPrefix(strs: string[]): string {
  const n = Math.min(...strs.map((i) => i.length));
  let res = "";

  for (let i = 0; i < n; i++) {
    const curr = strs[0][i];

    for (let s of strs) {
      if (s[i] !== curr) return res;
    }

    res += curr;
  }

  return res;
}
