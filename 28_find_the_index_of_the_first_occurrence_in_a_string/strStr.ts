function strStr(haystack: string, needle: string): number {
  const n = haystack.length;
  const m = needle.length;

  for (let i = 0; i < n - m + 1; i++) {
    if (haystack.slice(i, i + m) === needle) return i;
  }

  return -1;
}
