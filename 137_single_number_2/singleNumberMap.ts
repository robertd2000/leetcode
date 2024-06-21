function singleNumber(nums: number[]): number {
  const map = {};

  for (let num of nums) {
    const value = map[num];
    if (value) {
      map[num] = value + 1;
    } else {
      map[num] = 1;
    }
  }

  for (const [key, value] of Object.entries(map)) {
    if (value == 1) {
      return +key;
    }
  }

  return 0;
}
