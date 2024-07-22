function groupAnagrams(strs: string[]): string[][] {
  const hashMap = new Map();

  for (let s of strs) {
    const key = s.split("").sort().join("");

    if (hashMap.has(key)) {
      const value = hashMap.get(key);
      value.push(s);
    } else {
      hashMap.set(key, [s]);
    }
  }

  return Array.from(hashMap.values());
}
