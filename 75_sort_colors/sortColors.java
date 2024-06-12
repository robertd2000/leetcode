class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[4];

        for (int num : nums) {
            count[num]++;
        }

        int pos = 0;

        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0) {
                nums[pos] = i;
                count[i]--;
                pos++;
            }
        }
    }
}