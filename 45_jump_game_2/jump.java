class Solution {
    public int jump(int[] nums) {
        int reach = 0;
        int jumped = 0;
        int count = 0;
        int i = 0;

        while (i < nums.length - 1) {
            reach = Math.max(reach, nums[i] + i);

            if (i == jumped) {
                jumped = reach;
                count++;
            }
            i++;
        }

        return count;
    }
}