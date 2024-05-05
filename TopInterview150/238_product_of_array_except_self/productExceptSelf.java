class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int prefix = 1;
        int postfix = 1;

        Arrays.fill(result, 1);

        for (int i = 0; i < n; i++) {
            result[i] *= prefix;
            prefix *= nums[i];

            result[n - i - 1] *= postfix;
            postfix *= nums[n - i - 1];
        }

        return result;
    }
}