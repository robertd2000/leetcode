function lengthOfLongestSubstring(s: string): number {
  const n = s.length;

  if (n === 0) return 0;

  let max = 0;

  const map = new Map<string, number>();

  let j = 0;

  for (let i = 0; i < n; i++) {
    const char = s[i];
    if (map.has(char)) {
      j = Math.max(j, (map.get(char) || 0) + 1);
    }

    map.set(char, i);
    max = Math.max(max, i - j + 1);
  }

  return max;
}
