class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        if (matrix == null || m == 0 || n == 0) {
            return false;
        }

        int c = 0;
        int r = n - 1;

        while (c < m && r >= 0) {
            if (matrix[c][r] == target) {
                return true;
            }

            if (matrix[c][r] > target) {
                r--;
            } else {
                c++;
            }
        }

        return false;
    }
}