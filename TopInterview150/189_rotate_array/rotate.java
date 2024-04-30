class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        if (n == k) {
            return;
        }

        int r = k % n;

        reverse(nums, 0, n - 1);
        reverse(nums, 0, r - 1);
        reverse(nums, r, n - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}