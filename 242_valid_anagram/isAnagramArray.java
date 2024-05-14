class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if (n != m) {
            return false;
        }

        int[] counter = new int[26];

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            counter[c - 'a']++;
        }

        for (int i = 0; i < m; i++) {
            char c = t.charAt(i);
            counter[c - 'a']--;

            if (counter[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}