function longestCommonPrefix(strs: string[]): string {
  strs.sort();

  let res = "";

  const first = strs.at(0) || "";
  const last = strs.at(-1) || "";

  const n = Math.min(first.length, last.length);

  for (let i = 0; i < n; i++) {
    if (first[i] != last[i]) return res;

    res += first[i];
  }

  return res;
}
