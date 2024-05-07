class Solution {
    public boolean isSubsequence(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n > m) {
            return false;
        }

        if (n == 0) {
            return true;
        }

        int j = 0;

        for (int i = 0; i < m; i++) {
            if (j < n && s.charAt(j) == t.charAt(i)) {
                j++;
            }
        }

        return j == n;
    }
}