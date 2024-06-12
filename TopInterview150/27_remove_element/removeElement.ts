function removeElement(nums: number[], val: number): number {
  const count = new Array<number>(51).fill(0);

  for (let i of nums) {
    if (i !== val) {
      count[i]++;
    }
  }

  let pos = 0;

  for (let i = 0; i < count.length; i++) {
    while (count[i] > 0) {
      nums[pos] = i;
      count[i]--;
      pos++;
    }
  }

  return pos;
}
