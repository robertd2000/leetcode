function minimumRecolors2(blocks: string, k: number): number {
  const n = blocks.length;

  let black = 0;
  let res = n;

  for (let i = 0; i < n; i++) {
    if (i - k >= 0 && blocks[i - k] === "B") {
      black--;
    }

    if (blocks[i] === "B") {
      black++;
    }

    res = Math.min(res, k - black);
  }

  return res;
}
