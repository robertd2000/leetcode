function removeDuplicates(nums: number[]): number {
  let pos = 0;

  for (let i of nums) {
    if (pos < 2 || i != nums[pos - 2]) {
      nums[pos] = i;
      pos++;
    }
  }

  return pos;
}
