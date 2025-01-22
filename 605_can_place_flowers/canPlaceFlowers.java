class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int k = 0;
        int m = flowerbed.length;
        int start = flowerbed[0] == 0 ? 0 : 1;
        int end = flowerbed[m - 1] == 0 ? m : m - 1;

        for (int i = start; i < end; i++) {
            if ((i == 0 || flowerbed[i - 1] == 0) &&
                    flowerbed[i] == 0 &&
                    (i == m - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                k++;
            }
        }

        return k >= n;
    }
}