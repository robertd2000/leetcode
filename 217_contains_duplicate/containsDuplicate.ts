function containsDuplicate(nums: number[]): boolean {
  nums.sort();

  const n = nums.length;

  for (let i = 0; i < n - 1; i++) {
    if (nums[i] === nums[i + 1]) {
      return true;
    }
  }

  return false;
}
