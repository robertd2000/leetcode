function minIncrementForUnique(nums: number[]): number {
  const root = new Map();

  function find(x: number): number {
    const value = root.has(x) ? find(root.get(x) + 1) : x;
    root.set(x, value);
    return root.get(x);
  }

  return nums.reduce((a, v) => (a += find(v) - v), 0);
}
