class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int sum = 0;

        for (int num:nums) {
            if (sum < 0) sum = 0;
            sum += num;
            maxSum = Math.max(maxSum, sum);
        }
        
        return maxSum;
    }
}