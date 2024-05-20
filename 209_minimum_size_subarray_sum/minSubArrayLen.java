class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int j = 0;
        int i = 0;
        int sum = 0;
        int res = n + 1;

        while (j < n) {
            sum += nums[j];
            j++;

            while (sum >= target) {
                res = Math.min(res, j - i);
                sum -= nums[i];
                i++;
            }
        }

        return res <= n ? res : 0;
    }
}