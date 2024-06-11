function hIndex(citations: number[]): number {
  const n = citations.length;
  const count = new Array<number>(n + 1).fill(0);

  for (let i of citations) {
    if (i > n) {
      count[n]++;
    } else {
      count[i]++;
    }
  }

  let pos = 0;

  for (let i = 0; i <= n; i++) {
    for (let j = 0; j < count[i]; j++) {
      citations[pos] = i;
      pos++;
    }
  }

  let hIndex = 1;

  for (let i = n - 1; i >= 0; i--) {
    if (hIndex > citations[i]) {
      return hIndex - 1;
    }

    hIndex++;
  }

  return n;
}
