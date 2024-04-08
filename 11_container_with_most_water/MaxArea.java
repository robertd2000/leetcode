class Solution {
    public int maxArea(int[] height) {
        int max = 0;

        int l = 0;
        int r = height.length - 1;

        while (l < r) {
            int lH = height[l];
            int rH = height[r];

            int square = Math.min(lH, rH) * (r - l);

            if (square > max) {
                max = square;
            }

            if (lH < rH)
                l++;
            else
                r--;
        }

        return max;

    }
}