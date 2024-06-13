function majorityElement(nums: number[]): number {
  let count = 0;
  let candidate = 0;

  for (let num of nums) {
    if (count === 0) {
      candidate = num;
    }

    if (num === candidate) {
      count++;
    } else {
      count--;
    }
  }

  return candidate;
}
