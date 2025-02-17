function isAnagram(s: string, t: string): boolean {
  const n = s.length;
  const m = t.length;

  if (n !== m) return false;

  const hash = new Map<string, number>();

  for (const i of s) {
    const value = hash.get(i) || 0;
    hash.set(i, value + 1);
  }

  for (const i of t) {
    const value = hash.get(i) || 0;
    hash.set(i, value - 1);

    if (hash.has(i) && hash.get(i) < 0) {
      return false;
    }
  }

  return true;
}
