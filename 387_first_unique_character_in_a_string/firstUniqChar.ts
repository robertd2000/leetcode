function firstUniqChar(s: string): number {
  const hash = {};

  for (let i of s) {
    if (i in hash) {
      hash[i] += 1;
    } else {
      hash[i] = 1;
    }
  }

  for (let i of s) {
    if (hash[i] == 1) {
      return s.indexOf(i);
    }
  }

  return -1;
}
