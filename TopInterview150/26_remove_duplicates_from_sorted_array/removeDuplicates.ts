function removeDuplicates(nums: number[]): number {
  const count = new Array<number>(201).fill(0);

  for (let num of nums) {
    count[num + 100]++;
  }

  let pos = 0;

  for (let i = 0; i < count.length; i++) {
    if (count[i]) {
      nums[pos] = i - 100;
      pos++;
    }
  }

  return pos;
}
