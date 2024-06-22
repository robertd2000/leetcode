function hIndex(citations: number[]): number {
  const n = citations.length;
  let l = 0;
  let r = n - 1;

  while (l <= r) {
    let mid = Math.floor(l + (r - l) / 2);

    if (citations[mid] >= n - mid) {
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }

  return n - l;
}
