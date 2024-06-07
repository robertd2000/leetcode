class Solution {
    int[] nums;

    public Solution(int[] nums) {
        this.nums = nums;
    }

    public int[] reset() {
        return this.nums;
    }

    public int[] shuffle() {
        int[] shuffled = this.nums.clone();

        for (int i = shuffled.length - 1; i > 0; i--) {
            int temp = shuffled[i];
            int randomIdx = (int) Math.floor(Math.random() * (i + 1));

            shuffled[i] = shuffled[randomIdx];
            shuffled[randomIdx] = temp;
        }

        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
