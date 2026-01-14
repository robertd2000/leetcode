function longestConsecutive(nums: number[]): number {
  const numsSet = new Set(nums);
  let res = 0;

  for (let x of numsSet) {
    if (numsSet.has(x - 1)) continue;

    let y = x + 1;

    while (numsSet.has(y)) {
      y++;
    }

    res = Math.max(res, y - x);
  }

  return res;
}
