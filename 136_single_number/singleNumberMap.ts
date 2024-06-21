function singleNumber(nums: number[]): number {
  const n = nums.length;

  const map = {};

  for (let num of nums) {
    if (num in map) {
      map[num]++;
    } else {
      map[num] = 1;
    }
  }

  for (let [key, value] of Object.entries(map)) {
    if (value == 1) {
      return +key;
    }
  }

  return 0;
}
