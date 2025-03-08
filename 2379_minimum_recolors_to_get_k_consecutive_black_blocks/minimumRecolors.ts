function minimumRecolors(blocks: string, k: number): number {
  const n = blocks.length;
  let m = n;

  for (let i = 0; i < n - k + 1; i++) {
    let curr_m = 0;
    for (let j = i; j < k + i; j++) {
      if (blocks[j] === "W") curr_m++;
    }
    m = Math.min(m, curr_m);
  }

  return m;
}
