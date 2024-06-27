function lengthOfLongestSubstring(s: string): number {
  const map = {};
  const n = s.length;
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < n; right++) {
    if (!(s[right] in map) || map[s[right]] < left) {
      map[s[right]] = right;
      maxLength = Math.max(maxLength, right - left + 1);
    } else {
      left = map[s[right]] + 1;
      map[s[right]] = right;
    }
  }

  return maxLength;
}
