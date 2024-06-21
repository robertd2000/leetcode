function singleNumber(nums: number[]): number {
  let ones = 0;
  let twos = 0;

  for (let num of nums) {
    ones ^= num & ~twos;
    twos ^= num & ~ones;
  }

  return ones;
}
