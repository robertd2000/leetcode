class Solution {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            if (nums[left] + nums[right] == 0) {
                return nums[right];
            } else if (nums[left] + nums[right] < 0) {
                left++;
            } else {
                right--;
            }
        }

        return -1;
    }
}