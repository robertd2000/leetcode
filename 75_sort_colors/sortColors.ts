/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  const count = new Array<number>(4).fill(0);

  for (let num of nums) {
    count[num]++;
  }

  let pos = 0;

  for (let i = 0; i < count.length; i++) {
    for (let j = 0; j < count[i]; j++) {
      nums[pos] = i;
      pos++;
    }
  }
}
