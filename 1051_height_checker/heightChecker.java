class Solution {
    public int heightChecker(int[] heights) {
        int[] frequency = new int[101];

        for (int height : heights) {
            frequency[height]++;
        }

        int result = 0;
        int currentHeight = 0;

        for (int i = 0; i < heights.length; i++) {
            while (frequency[currentHeight] == 0) {
                currentHeight++;
            }

            if (heights[i] != currentHeight) {
                result++;
            }

            frequency[currentHeight]--;
        }

        return result;
    }
}