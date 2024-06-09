class Solution {
    public int uniquePaths(int m, int n) {
        return helper(m, n, new int[m + 1][n + 1]);
    }

    public int helper(int m, int n, int[][] arr) {
        if (m == 1 && n == 1) {
            return 1;
        }

        if (m < 1 || n < 1) {
            return 0;
        }

        if (arr[m][n] != 0) {
            return arr[m][n];
        }

        arr[m][n] = helper(m - 1, n, arr) + helper(m, n - 1, arr);
        return arr[m][n];
    }
}