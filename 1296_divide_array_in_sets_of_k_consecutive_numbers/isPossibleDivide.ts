function isPossibleDivide(nums: number[], k: number): boolean {
  const n = nums.length;

  if (n % k !== 0) return false;

  const map = {};

  for (let i of nums) {
    map[i] = map[i] ? map[i] + 1 : 1;
  }

  nums.sort((a, b) => a - b);

  for (let i of nums) {
    if (map[i] === 0) continue;

    for (let j = 0; j < k; j++) {
      const curr = i + j;

      if (!map[curr]) {
        return false;
      }

      map[curr]--;
    }
  }

  return true;
}
