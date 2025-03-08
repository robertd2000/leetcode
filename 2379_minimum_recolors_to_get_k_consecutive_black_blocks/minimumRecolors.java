class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();

        int black = 0;
        int res = n;

        for (int i = 0; i < n; i++) {
            if (i - k >= 0 && blocks.charAt(i - k) == 'B') black--;
            if (blocks.charAt(i) == 'B') black++;
            res = Math.min(res, k - black);
        }

        return res;
    }
}