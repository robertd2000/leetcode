class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int l = 0;
        int r = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            int val;
            if (Math.abs(nums[l]) > Math.abs(nums[r])) {
                val = nums[l];
                l++;
            } else {
                val = nums[r];
                r--;
            }

            res[i] = (int)Math.pow(val, 2);
        }

        return res;
    }
}