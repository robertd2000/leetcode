function rob(nums: number[]): number {
  if (nums.length == 0) return 0;

  let p1 = 0;
  let p2 = 0;

  for (let num of nums) {
    const tmp = p1;
    p1 = Math.max(p1, p2 + num);
    p2 = tmp;
  }

  return p1;
}
