class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int n = magazine.length();
        int m = ransomNote.length();
        if (m > n) {
            return false;
        }

        int[] counter = new int[26];

        for (int i = 0; i < n; i++) {
            char c = magazine.charAt(i);
            counter[c - 'a']++;
        }

        for (int i = 0; i < m; i++) {
            char c = ransomNote.charAt(i);
            if (counter[c - 'a'] == 0) {
                return false;
            }
            counter[c - 'a']--;
        }

        return true;
    }
}