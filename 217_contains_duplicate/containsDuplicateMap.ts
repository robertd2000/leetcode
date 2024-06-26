function containsDuplicate(nums: number[]): boolean {
  const map = {};

  for (let num of nums) {
    map[num] = map[num] ? map[num] + 1 : 1;

    if (map[num] > 1) return true;
  }

  return false;
}
