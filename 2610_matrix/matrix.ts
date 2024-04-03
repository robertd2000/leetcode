function findMatrix(nums: number[]): number[][] {
  const freq: number[] = Array(nums.length + 1).fill(0);
  const res: number[][] = [];

  nums.forEach((i) => {
    if (freq[i] >= res.length) {
      res.push([]);
    }

    res[freq[i]].push(i);
    freq[i]++;
  });

  return res;
}
