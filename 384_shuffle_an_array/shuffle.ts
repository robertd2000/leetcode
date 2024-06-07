class Solution {
  nums: number[];

  constructor(nums: number[]) {
    this.nums = nums;
  }

  reset(): number[] {
    return this.nums;
  }

  shuffle(): number[] {
    const shuffled = [...this.nums];
    const n = shuffled.length - 1;

    for (let i = n; i > 0; i--) {
      const temp = shuffled[i];
      const randomIndex = Math.floor(Math.random() * (i + 1));
      shuffled[i] = shuffled[randomIndex];
      shuffled[randomIndex] = temp;
    }

    return shuffled;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
