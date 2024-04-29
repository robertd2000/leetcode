class Solution {
    public boolean canJump(int[] nums) {
        int reach = 0;
        int n = nums.length;
        int i;
        
        for (i = 0; i < n && i <= reach; i++) {
            reach = Math.max(reach, i + nums[i]);
        }

        return i == n;
    }
}