function subarraysDivByK(nums: number[], k: number): number {
  const map = {
    0: 1,
  };

  let count = 0;
  let sum = 0;

  for (let i of nums) {
    sum = (sum + i) % k;

    if (sum < 0) sum += k;

    count += map[sum] || 0;
    map[sum] = map[sum] ? map[sum] + 1 : 1;
  }

  return count;
}
