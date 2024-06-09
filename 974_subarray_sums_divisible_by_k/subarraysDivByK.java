class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] count = new int[k];
        count[0] = 1;

        int res = 0;
        int sum = 0;

        for (int num : nums) {
            sum = (sum + num) % k;
            if (sum < 0) sum += k;
            res += count[sum]++;
        }

        return res;
    }
}
