function findDuplicate(nums: number[]): number {
  let n = nums.length;

  if (n < 1) return -1;

  let slow = nums[0];
  let fast = nums[nums[0]];

  while (slow != fast) {
    slow = nums[slow];
    fast = nums[nums[fast]];
  }

  fast = 0;

  while (slow != fast) {
    slow = nums[slow];
    fast = nums[fast];
  }

  return slow;
}
