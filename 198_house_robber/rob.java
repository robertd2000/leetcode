class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0)
            return 0;

        int p1 = 0;
        int p2 = 0;

        for (int num : nums) {
            int tmp = p1;
            p1 = Math.max(p1, p2 + num);
            p2 = tmp;
        }

        return p1;
    }
}